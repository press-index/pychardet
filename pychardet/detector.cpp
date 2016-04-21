#include "src/nsCharSetProber.h"
#include "detector.h"
#include <string.h>
#include <stdlib.h>

#ifndef MINIMUM_THRESHOLD
#define MINIMUM_THRESHOLD (float)0.20
#endif

UniversalDetectorWithConfidence::UniversalDetectorWithConfidence()
    : nsUniversalDetector(NS_FILTER_ALL)
    , m_charset(0)
    , m_confidence(0)
{
}

UniversalDetectorWithConfidence::~UniversalDetectorWithConfidence()
{
    if (m_charset)
    {
        free(m_charset);
    }
}

void UniversalDetectorWithConfidence::Report(const char* charset)
{
    if (m_charset)
    {
        free(m_charset);
    }
    m_charset = strdup(charset);

    m_confidence = 1;
}

void UniversalDetectorWithConfidence::Report(const char* charset, float confidence)
{
    if (m_charset)
    {
        free(m_charset);
    }
    m_charset = strdup(charset);

    m_confidence = confidence;
}

void UniversalDetectorWithConfidence::Reset()
{
    nsUniversalDetector::Reset();
    if (m_charset)
    {
        free(m_charset);
    }
    m_charset = strdup("");

    m_confidence = 0;
}

const char* UniversalDetectorWithConfidence::GetCharset() const
{
    return m_charset? m_charset : "";
}

float UniversalDetectorWithConfidence::GetConfidence()
{
    return m_confidence;
}

bool UniversalDetectorWithConfidence::IsDone()
{
    return mDone;
}

void UniversalDetectorWithConfidence::DataEnd()
{
    if (!mGotData)
    {
        // we haven't got any data yet, return immediately
        // caller program sometimes call DataEnd before anything has been sent to detector
        return;
    }

    if (mDetectedCharset)
    {
        mDone = PR_TRUE;
        Report(mDetectedCharset);
        return;
    }

    switch (mInputState)
    {
        case eHighbyte:
            {
                float proberConfidence;
                float maxProberConfidence = (float)0.0;
                PRInt32 maxProber = 0;

                for (PRInt32 i = 0; i < NUM_OF_CHARSET_PROBERS; i++)
                {
                    if (mCharSetProbers[i])
                    {
                        proberConfidence = mCharSetProbers[i]->GetConfidence();
                        if (proberConfidence > maxProberConfidence)
                        {
                            maxProberConfidence = proberConfidence;
                            maxProber = i;
                        }
                    }
                }
                //do not report anything because we are not confident of it,
                //that's in fact a negative answer
                if (maxProberConfidence > MINIMUM_THRESHOLD)
                {
                    Report(mCharSetProbers[maxProber]->GetCharSetName(), maxProberConfidence);
                }
            }
            break;
        case eEscAscii:
            break;
        default:
            break;
    }
}
