#include <iostream>

void swap(int& num1, int& num2){
    int temp;
    temp = num1; //save the value at address of num1 into temp
    num1 = num2; //put num2 into num1
    num2 = temp; //put temp (val num1) into num2

}

int main () {
   // local variable declaration:
   int a = 100;
   int b = 200;
 
   std::cout << "Before swap, value of a :" << a << std::endl;
   std::cout << "Before swap, value of b :" << b << std::endl;

   /* calling a function to swap the values using variable reference.*/
   swap(a, b);

   std::cout << "After swap, value of a :" << a << std::endl;
   std::cout << "After swap, value of b :" << b << std::endl;
 
   return 0;
}