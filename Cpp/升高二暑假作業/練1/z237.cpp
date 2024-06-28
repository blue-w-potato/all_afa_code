#include<iostream>
using namespace std;
main()
{
    int64_t a;
    cin>>a;
    int64_t b;
    cin>>b;
    int64_t c;
    c = 0;
    if(a>b){
        for( int i=b; i<=a; i++ ){
            c = c+i;
        }
    }
    else{
        
        for( int i=a; i<=b; i++ ){
            c = c+i;
        }
    }
    cout<<c;
}