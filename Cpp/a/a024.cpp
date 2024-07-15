#include <iostream>
using namespace std;
int main()
{
    int a, b = 0;
    cin >> a;
    while( a > 10 )
    {
        b = b + (a - a/10 * 10);
        a = a/10;
    }
    cout << b + a;
    return 0;
}