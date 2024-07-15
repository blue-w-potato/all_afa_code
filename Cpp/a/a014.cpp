#include<iostream>
using namespace std;
int main()
{
    int a;
    int b;
    int c;
    cin >> a >> b >> c;
    if( a > b )
    {
        a = b;
    }
    if( c > a )
    {
        c = a;
    }
    cout << c;
    return 0;
}