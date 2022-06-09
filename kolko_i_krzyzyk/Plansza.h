#pragma once

#include <iostream>

using namespace std;

class Plansza
{	
	friend class Gracz;
	friend class Czlowiek;
	friend class Maszyna;
	friend class Gra;
	int size;
	int** wsp;
public:

	Plansza();

	//~Plansza();
	void Wyswietl();
	
};

