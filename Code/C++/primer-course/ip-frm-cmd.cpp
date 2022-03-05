#include <iostream>

int main(int argc, char* argv[]){
    double a, sum=0;

    for (int i=1; i<argc; i++) {
        a =  std::atof(argv[i]);
        sum += a;    
    }

    std::cout << "Mean is " << sum/(argc-1) <<std::endl; 
    return 0;
}