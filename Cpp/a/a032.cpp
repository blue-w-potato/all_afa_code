#include<iostream>
using namespace std;

int main(){
    char a;
    int b, c;
    cin >> b >> a >> c;
    switch(a){

        case '+' :
        cout << b+c << endl;
        break;

        case '-' :
        cout << b-c << endl;
        break;

        case '*' :
        cout << b*c << endl;
        break;

        case '/' :
        cout << b/c << endl;
        break;

        default:
        cout<<endl;

    }


    return 0;
}