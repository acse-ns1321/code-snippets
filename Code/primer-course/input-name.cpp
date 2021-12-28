#include <iostream>

int main(){

    char name[256];

    std::cout << "What's your name?\n";
    std::cin >> name;
    std::cout << "Hello " << name << "!\n";

    return 0;
}