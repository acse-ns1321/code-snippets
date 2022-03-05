// File: childClassName.h

#include <string>       // <--- Explicitly include the string header, even though yourClassName.h also includes it

#include "class.h"	// <--- You must include the declaration in order to extend the class

// We extend from yourClassName by using the colon (:) and specifying which type of inheritance
// will be used (public inheritance, in this case)

class childClassName : public yourClassName {
private:
    int cs_private_variable;
    int cs_private_variable2;

    // <--- NOTE: The member variables 'private_variable' and 'private_variable2' are already inherited from yourClassName
    //            it's as if we sort of get them for free, since we are a sub-class

public:
    // Constructors
    explicit childClassName(const std::string &private_variable2);
    childClassName(const std::string &name, const int cs_private_variable, const int cs_private_variable2);

    // Getters and Setters
    const int getMethodCC(void) const { return this->cs_private_variable; }
    void setMethodCC(const int) { this->cs_private_variable = cs_private_variable; }

    const int getMethodCC2(void) const { return this->cs_private_variable2; }
    void setMethodCC(const int) { this->cs_private_variable2 = cs_private_variable2; }

    // <--- NOTE: Again, the getters/setters for 'private_variable' and 'private_variable2' are already inherited from yourClassName

    // Other Methods
    const int Area(void) const;
};