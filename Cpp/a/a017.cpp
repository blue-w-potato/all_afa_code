#include<iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    if( n >= 90 )
    {
        cout << "A";
    }
    else if( n >= 80 )
    {
        cout << "B";
    }
    else if( n >= 70 )
    {
        cout << "C";
    }
    else if( n >= 60 )
    {
        cout << "D";
    }
    else{
        cout << "E";
    }
    return 0;
}
/*
90分(含)~100分(含)為A等
80分(含)~90分(不含)為B等
70分(含)~80分(不含)為C等
60分(含)~70分(不含)為D等
不滿60分者為E等
*/