#pragma once

#include <string>
#include <iostream>
#include "Plansza.h"

using namespace std;

class Gracz
{	
public:
	string name;
	int symbol;
	
	Gracz();

	void ruch(Plansza&);
	void symbole(Gracz&);
};

