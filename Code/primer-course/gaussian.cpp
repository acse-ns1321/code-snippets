#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

int main(){
    double x,m,s,g;
    std::cout<<"Input x,m and s"<<std::endl;
    std::cin>>x>>m>>s;
    g = (1/(s*sqrt(2*M_PI)))*exp(pow(-0.5*(x-m)/s, 2));
    std::cout<<"The gaussian is :"<<g<<std::endl;
    return 1;
}