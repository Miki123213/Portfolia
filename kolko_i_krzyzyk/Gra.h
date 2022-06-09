#pragma once

#include "Plansza.h"
#include "Gracz.h"
#include "Maszyna.h"
#include <iostream>

using namespace std;

class Gra
{
public:
	int wynik;
	Gra();
	~Gra();
	void sprawdzenie(Plansza&, Gracz&, Gracz&);
};

