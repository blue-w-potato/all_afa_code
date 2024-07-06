#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    long long  a=0;
    long long  b=1;
    cout<<a<<" "<<b<<" ";
    if(n>2){
        long long  c;
        for(int i=0; i<n-2; i++){
            c=a+b;
            cout<<c<<" ";
            a=b+0;
            b=c+0;
        }
    }
    return 0;
}