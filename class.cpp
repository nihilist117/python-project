#include<iostream>
using namespace std;

class abhijith {  // abhijith is a class
public:
    int a;       // a is a class variable
    float b;
};   

int main() {
    abhijith a1;  // here a1 is a object
    a1.a = 5;
    a1.b = 4.5;

    cout << a1.a;
    cout << a1.b;
    return 0;
}