#include <string>
#include <iostream>

#include "class.h"    // <--- Obtains the class declaration

int main(int argc, char * argv[]) {
    
    // Create an instance of the class 
    yourClassName class1 = class1(0, "String input");

    // Get default parametrs of the class
    std::cout << class1.getMethod() << class1.getMethod2() << std::endl;

    // Change parameters of the class
    class1.setMethod(3);
    class1.setMethod2("Another string");
}