#include<iostream>
using namespace std;
int main(){
    string a,b="";
    int c;
    cin >> a;
    c = a.length();
    for( int i=0; i<c; i++ ){
        b = a[i]+b;
    }
    cout << b;

    return 0;
}