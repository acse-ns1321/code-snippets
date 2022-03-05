
#include <string>	// <--- Required for std::string

#include "class.h"    // <--- Obtains the class declaration

// Constructor
yourClassName::yourClassName(const int private_variable, const std::string & private_variable2) {
    this->private_variable = private_variable;	// 'this' is a pointer to the instance of the class. Members are accessed via the -> operator
    this->private_variable2 = private_variable2;			// In this case you need to use 'this->...' to avoid shadowing the member variable since the argument shares the same name
}
// Member initialization lists
className(const int private_variable1, const int private_variable2, const std::string & private_variable3) 
        : private_variable1(private_variable1), private_variable2(private_variable2), private_variable3(private_variable3) {}
// Get 
int yourClassName::getMethod(void) const {	// The 'const' here tells the compiler that you guarantee that you won't modify the object when this function is called. This allows it to perform optimizations that it otherwise may not be able to do
    return this->private_variable;
}

// Set 
void yourClassName::setMethod(const int private_variable) {
    this->private_variable = private_variable;
}


}