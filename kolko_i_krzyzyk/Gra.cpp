#include "Gra.h"

Gra::Gra()
{
	wynik = 0;
}

Gra::~Gra()
{

}

void Gra::sprawdzenie(Plansza& p, Gracz& a, Gracz& b)
{
	int r = 0;
	int k = p.size - 1;
	int xpoz = 0;
	int xpion = 0;
	int xskos = 0;
	int opoz = 0;
	int opion = 0;
	int oskos = 0;
	for (int i = 0; i < p.size; i++)
	{

		xpoz = 0;
		opoz = 0;
				
		for (int j = 0; j < p.size; j++)
		{
			if (p.wsp[i][j] != 0)
			{
				r++;
				if (p.wsp[i][j] == 1)
					xpoz++;
				else
					opoz++;
			}			
		}
		if (r == p.size * p.size)
		{
			wynik = 1;
		}
		else if (xpoz == p.size || opoz == p.size)
		{
			wynik = 2;
			break;
		}
	}
	if (wynik != 2)
	{
		for (int i = 0; i < p.size; i++)
		{
			xpion = 0;
			opion = 0;
			for (int j = 0; j < p.size; j++)
			{
				if (p.wsp[j][i] == 1)
				{
					xpion++;
				}
				else if (p.wsp[j][i] == 2)
				{
					opion++;
				}
			}
			if (xpion == p.size || opion == p.size)
			{
				wynik = 2;
				break;
			}
		}
	}
	
	if (wynik != 2)
	{
		for (int i = 0; i < p.size; i++)
		{
			if (p.wsp[i][i] == 1)
			{
				xskos++;
			}
			else if (p.wsp[i][i] == 2)
			{
				oskos++;
			}
			if (xskos == p.size || oskos == p.size)
			{
				wynik = 2;
			}
		}
	}
	
	if (wynik != 2)
	{
		xskos = 0;
		oskos = 0;
		for (int i = 0; i < p.size; i++)
		{
			if (p.wsp[k][i] == 1)
			{
				xskos++;
			}
			else if (p.wsp[k][i] == 2)
			{
				oskos++;
			}
			if (xskos == p.size || oskos == p.size)
			{
				wynik = 2;
			}
			k--;
		}
	}

	if (wynik == 1)
	{
		cout << "REMIS";
	}
	else if (wynik == 2)
	{
		cout << "ZWYCIEZA GRACZ: ";
		if (xpoz == p.size || xpion == p.size || xskos == p.size)
		{
			if (a.symbol == 1)
				cout << a.name;
			else if (b.symbol == 1)
				cout << b.name;
		}
		else if (opoz == p.size || opion == p.size || oskos == p.size)
		{
			if (a.symbol == 2)
				cout << a.name;
			else if (b.symbol == 2)
				cout << b.name;
		}
	}

}



