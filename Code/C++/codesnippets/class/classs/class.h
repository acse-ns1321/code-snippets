#include <string>

class yourClassName {
// Private members and methods - accessible via methods in the class definition
private:
    int private_variable; 
    std::string private_variable2;   	

// Protected members and methods - accessible in the class definition or by classes who extend this class
protected:
    std::string protected_variable;   

// Public members and methods - accessible to anyone who creates an instance of the class
public:
    // get
    int getMethod(void) const { return this->private_variable; }
    void setMethod(const int private_variable) { this->private_variable = private_variable; }
    //set
    std::string & getMethod2(void) const { return this->private_variable2; }  
    void setMethod2(const std::string & private_variable2) { this->private_variable2 = private_variable2; }
};