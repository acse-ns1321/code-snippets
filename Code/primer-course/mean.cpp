#include <iostream>

int main(){
    int n;
    double a, sum=0;

    std::cout << "How many numbers would you like to enter?\n";
    std::cin >> n;

    for (int i=0; i<n; i++) {
        std::cout << "Enter number " << i+1 << std::endl ;
        std::cin >> a;
        sum += a;    
    }

    std::cout << "Mean is " << sum/n; 
    return 0;
}