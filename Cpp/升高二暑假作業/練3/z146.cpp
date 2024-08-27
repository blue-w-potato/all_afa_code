#include<iostream>
using namespace std;
int main(){
    long a,c,s=0;
    cin >> a;
    for( long i=1; i<=a; i++ ){
        c = i/5;
        if( c*5 == i ) {
            s+=i;
        }
        
    }
    cout << s << endl;

    return 0;
}