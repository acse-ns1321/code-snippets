#include <iostream>

int main(){
int *a;
int b = 7; // B is a normal int variable holding the value 7
a = &b; // point

std::cout << a << std::endl;; // returns b's memory address.
std::cout << *a << std::endl; // returns b's value  (i.e. 7).

*a = 10;                     // updates a's target
std::cout << b << std::endl; // returns 10
return 1;
}