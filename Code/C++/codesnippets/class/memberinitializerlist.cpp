class className {
private:
    int private_variable1;
    int private_variable2;
    std::string private_variable3;

public:
    className(const int private_variable1, const int private_variable2, const std::string & private_variable3) 
        : private_variable1(private_variable1), private_variable2(private_variable2), private_variable3(private_variable3) {}
};