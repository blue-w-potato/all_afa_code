#include <iostream>
using namespace std;
int main()
{
    int a, b, c;
    cin >> a >> b;
    c = 0;
    if( b == 2 || b == 5 || b == 8 )
    {
        c = 200;
    }
    else if( a - ( a/2 )*2 != 0 )
    {
        c = 100;
    }
    else if( a == b )
    {
        c = 50;
    }
    cout << c;
    return 0;
}