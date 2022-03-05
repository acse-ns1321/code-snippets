#include <iostream>
using namespace std;


template <class T>      // <--- 'class' is synonymous with 'typename'
class Container {
private:
    T data;
public:
    explicit Container(const T & d) : data(d) {}
};

// Usage
int main() {
    Container<int> a(1);
    Container<float> b(10.0f);
    Container<Container<int>> c(a);
}



//------------ TWO TEMPLATE VARIABLES----------------------------------------

template<class T, class U>
class A {
	T x;
	U y;
public:
	A() { cout<<"Constructor Called"<<endl; }
};

int main() {
A<char, char> a;
A<int, double> b;
return 0;
}
