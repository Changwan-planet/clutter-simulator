#include "Chirp.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

/// MAIN FUNCTION ///
int main(int argc, char *arg[])
{
    Chirp chirpSignal(3.75 * pow(10,6), 3 * pow(10, -6));
    cout << "Inital Frequency: " << chirpSignal.getInitFreq() << endl;
    cout << "Delta Time: " << chirpSignal.getDeltaTime() << endl;
    return 0;
}