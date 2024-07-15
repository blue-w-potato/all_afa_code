#include <iostream>
using namespace std;
int main()
{
    int a, b, c = 0;
    cin >> a >> b;
    while( a < b )
    {
        a = a*3;
        c = c+1;
    }
    cout << c;
    return 0;
}