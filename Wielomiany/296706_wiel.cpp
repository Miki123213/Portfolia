#include "wiel.h"

using namespace std;

int main()
{
    int tab[6] = { 1,-5,1,-3,1,2 };
    int tab2[5] = { -5,1,-3,1,2 };
    wiel x(tab, 6);
    wiel y(tab2, 5);
    wiel z;
    char a[] = "200x+6x^35-x^37-5+5x^1500";
    char b[] = "2x+5";
    wiel c(a);
    x.Add(&y)->Wyswietl();
    cout << endl;
    cout << *x.Add(&y) << endl;
    cout << "X = " << x << endl;
    cout << "Y = " << y << endl;
    cout << "Y - X = " << y - x << endl;
    z = x * y * c;
    cout << "Z = X * Y * C = " << z << endl;
    cout << "wiel(b) = " << wiel(b) << endl;
    cout << "C = " << c << endl;
    cout << "C - C = " << c - c << endl;
    c -= x;
    cout << "C -= X: " << c << endl;
    c += wiel(b);
    cout << "c += wiel(b): " << c << endl;

}
