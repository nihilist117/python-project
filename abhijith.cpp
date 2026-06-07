#include<iostream>
#include<cmath>
using namespace std;
double add(double n1,double n2){
    return n1 + n2;
}
double subtract(double n1,double n2){
    return n1 - n2;
}
double multiply(double n1,double n2){
    return n1*n2;
}
double division(double n1,double n2){
    if(n2 == 0){
        cout<<"invalid number";
        return 0;
    }
    
        return n1/n2;
}
double power(double n1,double n2){
    return pow(n1,n2);
}
double