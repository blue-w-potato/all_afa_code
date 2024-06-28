#include<iostream>
#include<math.h>
using namespace std;
main(){
    double r;
    cin>>r;
    float pi=3.1415926535;
    cout<<"Radius = ";
    printf("%0.2f\n", r);

    double perimeter = r*2*pi;
    perimeter = perimeter/0.01;
    perimeter = round(perimeter);
    perimeter = perimeter*0.01;
    cout<<"Perimeter = ";
    printf("%0.2f\n", perimeter);

    double area = r*r*pi;
    area = area/0.01;
    area = round(area);
    area = area*0.01;
    cout<<"Area = ";
    printf("%0.2f\n", area);
}