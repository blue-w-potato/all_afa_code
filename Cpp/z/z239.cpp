#include<iostream>
using namespace std;
main(){
    char a;
    cin>>a;
    int b;
    cin>>b;
    int c;
    cin>>c;
    for( int i=0; i<c; i++ ){
        for( int j=0; j<b; j++ ){
            cout<<a<<" ";
        }
        cout<<endl;
    }
}