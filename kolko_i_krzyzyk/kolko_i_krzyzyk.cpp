#include <iostream>
#include <Windows.h>
#include "Plansza.h"
#include "Gracz.h"
#include "Gra.h"
#include "Czlowiek.h"
#include "Maszyna.h"

using namespace std;

void rozgrywka()
{
	int i = 1;
	Gra g;
	Plansza a;
	Maszyna b; // Wpisać człowiek lub maszyna
	Maszyna c; // Wpisać człowiek lub maszyna
	b.symbole(c);
	while (true)
	{
		cout << endl << "Runda: " << i << endl;
		b.ruch(a);
		a.Wyswietl();
		g.sprawdzenie(a, b, c);
		if (g.wynik != 0)
		{
			break;
		}
		Sleep(500);
		c.ruch(a);
		a.Wyswietl();
		g.sprawdzenie(a, b, c);
		if (g.wynik != 0)
		{
			break;
		}
		Sleep(500);
		i++;
	}
}

int main()
{
	
	rozgrywka();

	
}

