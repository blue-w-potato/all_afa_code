#include<iostream>
using namespace std;
int main()
{
    char a[100];
    char b[100];
    char c[100];
    cin.getline(a,100);
    cin.getline(b,100);
    cin.getline(c,100);
    cout<<"Department: "<<a<<endl;
    cout<<"Student ID: "<<b<<endl;
    cout<<"Name: "<<c<<endl;
}