#include<iostream>
using namespace std;
int main(){
    int a,b,c,s=0;
    cin >> a >> b;
    for( int i=a; i<=b; i++ ){
        c = i/2;
        if( c*2 == i ) {
            s+=i;
        }
        
    }
    cout << s << endl;

    return 0;
}