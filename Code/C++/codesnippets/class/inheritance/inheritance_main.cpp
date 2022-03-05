#include <iostream>

#include "Inheritance.h"

int main(int argc, char *argv[]) {
    childClassName childInstance = childInstance("Square", 6, 6);

    std::cout << childInstance.getMethod2() << childInstance.getMethod() << childInstance.Area() << std::endl;
}