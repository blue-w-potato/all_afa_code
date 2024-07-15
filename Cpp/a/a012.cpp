#include<iostream>
using namespace std;
int main()
{
    float n;
    int m;
    cin >> n;
    m = n/2;
    if( n/2 == m )
    {
        cout << "EVEN";
    }
    else
    {
        cout << "ODD";
    }
    return 0;
}