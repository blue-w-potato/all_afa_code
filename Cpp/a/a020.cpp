#include <iostream>
using namespace std;
int main()
{
    int a, b, c;
    cin >> a >> b;
    c = 0;
    if( b == 2 || b == 5 || b == 8 )
    {
        c = c + 200;
    }
    if( a - ( a/2 )*2 != 0 )
    {
        c = c + 100;
    }
    if( a == b )
    {
        c = c + 50;
    }
    cout << c;
    return 0;
}