// File: childClassName.cpp

#include "childClassName.h"	// <--- Only need to include 'childClassName', since 'yourClassName' is included in 'inheritance.h'

// This constructor calls the superclass (yourClassName) constructor and sets the private_variable2 and number of sides to '4', and then sets the cs_private_variable and cs_private_variable2
childClassName::childClassName(const std::string &private_variable2, const int cs_private_variable, const int cs_private_variable2) : yourClassName(4, private_variable2) {
    this->cs_private_variable = cs_private_variable;
    this->cs_private_variable2 = cs_private_variable2;
}

// This constructor calls the superclass (yourClassName) constructor, but sets the cs_private_variable and cs_private_variable2 to a constant value
// The explicit keyword is used to restrict the use of the constructor
explicit childClassName::childClassName(const std::string &private_variable2) : yourClassName(4, private_variable2) {
    this->cs_private_variable = 1;
    this->cs_private_variable2 = 1;
}

// Compute the area of the childClassName
int childClassName::Area(void) const {
    return cs_private_variable * cs_private_variable2;		// <--- Note that you don't explicitly need 'this->', you can directly use the member variables
}