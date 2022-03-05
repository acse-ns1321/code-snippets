#include <iostream>
#include <string>

int i;
float f;
double d;
std::string str;

try {
    // string -> integer
    int i = std::stoi(str);

    // string -> float
    float f = std::stof(str);

    // string -> double 
    double d = std::stod(str);
} catch (...) {
    // error management
}   