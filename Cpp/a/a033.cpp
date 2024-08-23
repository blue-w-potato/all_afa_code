#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    cin >> a;

    cout << '|';
    
    cout << "____";

    if( a.length() < 4 ){
        for( int i=0; i<( 4-a.length() ); i++ ){
            cout << '_';
        }
        cout << a;
    }
    else{
        cout << a.substr( a.length()-4, a.length()-1 );
    }

    cout << '|';

    return 0;
}