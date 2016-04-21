# coding=utf-8
cdef extern from "src/nscore.h":
    enum nsresult:
        NS_OK
        NS_ERROR_OUT_OF_MEMORY


cdef extern from "detector.h":
    cdef cppclass UniversalDetectorWithConfidence:
        UniversalDetectorWithConfidence()
        const char* GetCharset()
        float GetConfidence()
        nsresult HandleData(const char* buf, size_t buf_len)
        void Reset()
        void DataEnd()
        bint IsDone()


cdef class UniversalDetector:
    cdef UniversalDetectorWithConfidence *instance

    def __cinit__(self):
        self.instance = new UniversalDetectorWithConfidence()

    def __dealloc__(self):
        del self.instance

    property done:
        def __get__(self):
            return self.instance.IsDone()

    property result:
        def __get__(self):
            cdef bytes encoding = <bytes> self.instance.GetCharset()
            cdef float confidence = self.instance.GetConfidence()

            return {
                'encoding': encoding.decode().lower() if encoding else None,
                'confidence': confidence
            }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def feed(self, bytes byte_str):
        cdef nsresult res = self.instance.HandleData(byte_str, len(byte_str))

        if res == NS_ERROR_OUT_OF_MEMORY:
            raise MemoryError('Out of memory')

        self.instance.DataEnd()

    def close(self):
        self.instance.Reset()
