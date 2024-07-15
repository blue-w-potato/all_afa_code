#include <iostream>
using namespace std;
int main()
{
    int a, b, c = 0;
    cin >> a >> b;
    if( a > b )
    {
        for( int i = a; i>=b; i-- )
        {
            cout << i;
            c = c + i;
            if( i != b )
            {
                cout << "+";
            }
            else{
                cout << "=" << c;
            }
        }
    }
    else
    {
        for( int i = a; i<=b; i++ )
        {
            cout << i;
            c = c + i;
            if( i != b )
            {
                cout << "+";
            }
            else{
                cout << "=" << c;
            }
        }
    }
    return 0;
}