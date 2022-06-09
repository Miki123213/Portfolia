#include "Plansza.h"

Plansza::Plansza()
{
	cout << "Podaj rozmiar pola do gry: ";
	cin >> size;
	wsp = new int* [size];

	for (int i = 0; i < size; i++)
	{
		wsp[i] = new int[size];
	}


	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			wsp[i][j] = 0;
		}
	}
	Wyswietl();
}
/*
Plansza::~Plansza()
{
	for (int i = 0; i < size; i++)
	{
		delete[] wsp[i];
	}		
	delete[] * wsp;
}*/

void Plansza::Wyswietl()
{
	cout << endl << "  ";
	for (int k = 0; k < size; k++)
	{
		cout << "  " << k << " ";
	}
	cout << endl;
	for (int i = 0; i < size; i++)
	{
		cout << i << " ";
		for (int j = 0; j < size; j++)
		{
			if (wsp[i][j] == 0)
			{
				cout << "|   ";
			}
			if (wsp[i][j] == 1)
			{
				cout << "| x ";
			}
			if (wsp[i][j] == 2)
			{
				cout << "| o ";
			}
		}
		cout << "|" << endl;
	}
	cout << endl;
}