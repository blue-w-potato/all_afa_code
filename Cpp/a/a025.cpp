#include <iostream>
using namespace std;
int main()
{
    int a, b = 0;
    cin >> a;
    while( a > 10 )
    {
        b = b*10 + ( a - a/10 * 10 );
        a = a/10;
    }
    cout << b*10 + a;
    return 0;
}