#include "Maszyna.h"

Maszyna::Maszyna():Gracz()
{

}

void Maszyna::ruch(Plansza& a)
{
	cout << "Tura gracza: " << name;
	if (symbol == 1)
		cout << " (x)" << endl;
	else
		cout << " (o)" << endl;
	int i, j;
	srand(time(NULL));
	i = rand() % a.size;
	j = rand() % a.size;
	while (a.wsp[i][j] != 0)
	{
		i = rand() % a.size;
		j = rand() % a.size;
	}
	a.wsp[i][j] = symbol;
}