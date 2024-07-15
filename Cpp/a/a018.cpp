#include<iostream>
using namespace std;
int main()
{
    int a;
    int b;
    cin >> a >> b;
    if( 14*60 + 20 <= a*60 +b && a*60 + b <= 16*60 + 40 )
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}