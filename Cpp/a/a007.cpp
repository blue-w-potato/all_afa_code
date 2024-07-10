#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a;
    int b;
    a = n/60/1;
    b = n-a*60;
    cout<<a<<" "<<b;
    return 0;
}