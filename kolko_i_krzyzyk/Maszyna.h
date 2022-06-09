#pragma once
#include "Gracz.h"
class Maszyna : public Gracz
{
public:
	Maszyna();

	virtual void ruch(Plansza&);
};

