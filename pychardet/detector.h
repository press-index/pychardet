#include "src/nscore.h"
#include "src/nsUniversalDetector.h"

class UniversalDetectorWithConfidence : public nsUniversalDetector {
    protected:
        char *m_charset;
        float m_confidence;

        virtual void Report(const char* charset);

        void Report(const char* charset, float confidence);

    public:
        UniversalDetectorWithConfidence();

        virtual ~UniversalDetectorWithConfidence();

        virtual void Reset();

        virtual void DataEnd();

        const char* GetCharset() const;

        float GetConfidence();

        bool IsDone();
};
