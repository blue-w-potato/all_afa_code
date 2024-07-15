#include <iostream>
using namespace std;
int main()
{
    int a, b, c = 1;
    cin >> a >> b;
    for( int i = a - b + 1; i<=a; i++ )
    {
        c = c*i;
    }
    cout << c;
    return 0;
}