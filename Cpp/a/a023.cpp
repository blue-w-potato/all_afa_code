#include <iostream>
using namespace std;
int main()
{
    int a, b = 1;
    cin >> a;
    while( a > 1)
    {
        if( a - ( a/2 )*2 == 0)
        {
            a = a/2;
        }
        else
        {
            a = a*3 +1;
        }
        b = b+1;
    }
    cout << b;
    return 0;
}