#include <iostream>
using namespace std;
int main()
{
    int a;
    cin >> a;
    while( a - ( a/2 )*2 == 0 )
    {
        a = a/2;
    }
    cout << a;
    return 0;
}