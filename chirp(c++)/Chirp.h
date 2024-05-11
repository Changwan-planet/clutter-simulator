#pragma once
#ifndef CHIRP_H
#define CHIRP_H
#include <math.h>

class Chirp
{
private:
    float initFreq;
    float freqSlope;
    float *chirp;
    float deltaTime;

public:
    //Constructor
    Chirp();
    Chirp(float initFreq, float deltatime);
    //Setters
    void setInitFreq(float initFreq);
    void setFreqSlope(float freqSlope);
    void setChirp(float *chirp);
    void setDeltaTime(float deltaTime);
    //Getters
    float getInitFreq();
    float getFreqSlope();
    float *getChirp();
    float getDeltaTime();
    //Methods
    void calculateSlope(float deltaFreq);
    void generateChirp(float sampleInterval);
};

#endif