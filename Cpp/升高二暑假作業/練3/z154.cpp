#include<iostream>
using namespace std;
int main(){
    long a,b=1;
    cin >> a;
    for( long i=1; i<=a; i++ ){
        b*=i;
    }
    cout << b;

    return 0;
}