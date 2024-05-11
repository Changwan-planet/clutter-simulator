#include "Chirp.h"

Chirp::Chirp()
{
    initFreq = 0;
    freqSlope = 0;
    chirp = NULL;
    deltaTime = 0;
}
Chirp::Chirp(float initFreq, float deltaTime)
{
    this->initFreq = initFreq;
    this->deltaTime = deltaTime;
    chirp = NULL;
}

//Setters
void Chirp::setInitFreq(float initFreq)
{
    this->initFreq = initFreq;
}
void Chirp::setFreqSlope(float freqSlope)
{
    this->freqSlope = freqSlope;
}
void Chirp::setChirp(float *chirp)
{
    this->chirp = chirp;
}
void Chirp::setDeltaTime(float deltaTime)
{
    this->deltaTime = deltaTime;
}

//Getters
float Chirp::getInitFreq()
{
    return initFreq;
}
float Chirp::getFreqSlope()
{
    return freqSlope;
}
float *Chirp::getChirp()
{
    return chirp;
}
float Chirp::getDeltaTime()
{
    return deltaTime;
}

//Method
void Chirp::calculateSlope(float deltaFreq)
{
    freqSlope = deltaFreq / (deltaTime * 2);
}
void Chirp::generateChirp(float sampleInterval)
{
    int numChirpSamples = int(deltaTime / sampleInterval);
    float currentTime = 0;

    chirp = new float[numChirpSamples];
    for (int i = 0; i < numChirpSamples; i++)
    {
        currentTime = i * sampleInterval;
        chirp[i] = sin(2 * M_PI * (initFreq - freqSlope * currentTime) * currentTime);
    }
}