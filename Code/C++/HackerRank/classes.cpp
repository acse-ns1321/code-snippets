#include <iostream>
#include <sstream>
using namespace std;

class Student{
    
    // private access specifier for variables of a class (unlike strusts)
    private:
    int age;
    int standard;
    string first_name;
    string last_name;
    
    // Creating public setter and getter functions for each element
    public:
    // Construct the class
    Student(){}
    
    // Setter functions
    // take in the input parameter
    void set_age(int age){
        this->age = age;
    }
    void set_standard(int standard){
        this->standard = standard;
    }
    void set_first_name(string first_name){
        this->first_name = first_name;
    }
    void set_last_name(string last_name){
        this->last_name = last_name;
    }
    
    // getter functions
    // no input parameters
    int get_age(){
        return age;
    }
    string get_first_name(){
        return first_name;
    }
    string get_last_name(){
        return last_name;
    }
    int get_standard(){
        return standard;
    }
    
    // to_string function
    
    string to_string(){
        string output = std::to_string(age) + "," + first_name + "," + last_name + "," + std::to_string(standard);
        return output;
    }
    // Destruct the class
    ~Student() {}   
};
int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}