#include "Gracz.h"


Gracz::Gracz()
{
	string a;
	cout << "Podaj nazwe gracza: ";
	cin >> name;
	cout << "Wybierz symbol (x lub o): ";
	cin >> a;
	while (true)
	{
		if (a == "x")
		{
			symbol = 1;
			break;
		}			
		else if (a == "o")
		{
			symbol = 2;
			break;
		}			
		else
		{
			cout << "Nieprawidlowy symbol. Wybierz jeszcze raz.";
			cin >> a;
		}
	}

	cout << name << " - " << a << endl;
}

void Gracz::ruch(Plansza& a)
{
	cout << "Tura gracza: " << name;
	if (symbol == 1)
		cout << " (x)" << endl;
	else
		cout << " (o)" << endl;
	int i, j;
	cout << "Podaj wiersz i kolumne pola do ktorego chcesz zapisac znak: ";
	cin >> i >> j;
	while ((i < 0 || i >= a.size) || (j < 0 || j >= a.size))
	{
		cout << "Niepoprawne wartosci. Podaj jeszcze raz upewniajac sie, ze nie przekraczaja " << a.size - 1 << endl;
		cin >> i >> j;
	}
	while (a.wsp[i][j] != 0)
	{
		cout << "To pole jest zajete. Podaj inne: ";
		cin >> i >> j;
	}
	a.wsp[i][j] = symbol;

	
}

void Gracz::symbole(Gracz& a)
{
	string i;
	if (symbol == a.symbol)
	{
		cout << "Wybrano identyczne symbole dla obu graczy. Nalezy ponownie dokonac wyboru" << endl;
		cout << "Symbol dla gracza " << name << ": ";
		cin >> i;
		while (true)
		{
			if (i == "x")
			{
				symbol = 1;
				break;
			}
			else if (i == "o")
			{
				symbol = 2;
				break;
			}
			else
			{
				cout << "Nieprawidlowy symbol. Wybierz jeszcze raz.";
				cin >> i;
			}
		}
		if (symbol == 1)
			a.symbol = 2;
		else
			a.symbol = 1;

		cout << "Gracz: " << name << " - " << i << endl;
		cout << "Gracz: " << a.name << " - ";
		if (a.symbol == 1)
			cout << "x" << endl;
		else
			cout << "o" << endl;
	}		
}