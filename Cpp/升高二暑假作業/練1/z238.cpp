#include<iostream>
using namespace std;
main()
{
    int64_t a;
    cin>>a;
    int64_t b;
    cin>>b;
    int64_t c;
    c = 1;
    for(int i=0;i<b;i++){
        c = c*a;
    }
    cout<<c<<endl;
}