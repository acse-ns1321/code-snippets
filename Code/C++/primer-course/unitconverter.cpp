/* A unit converter
Write a C++ program to take in an input in metres and return the 
distance in feet and/or inches. Remember that one inch is 2.54 cm, and that one foot is 12 inches. */

#include <iostream>
#include <stdio.h>
int main(){
    double m;
    std::cout<<"Enter your value in meters"<<std::endl;
    std::cin>>m;
    std::cin.ignore();
    double i = m*1000/2.54;
    double f = i/12;
    std::cout<<"Inches:"<<i<<std::endl;
    std::cout<<"Feet:"<<f<<std::endl;
    return 0;
}