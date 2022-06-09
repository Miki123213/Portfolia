#include "wiel.h"
#include <string>

using namespace std;

// KONSTRUKTORY
wiel::wiel()
{
	size = 0;
	wsp = 0;
}

wiel::wiel(int* t, int s)
{
	wsp = new int[s];
	memcpy(wsp, t, sizeof(int) * s);
	size = s;
}

wiel::wiel(wiel& y)
{
	wsp = new int[y.size];
	memcpy(wsp, y.wsp, sizeof(int) * y.size);
	size = y.size;
}

wiel::wiel(char* a)
{
	char* w1;
	char* w2;
	char* w3;
	char* w4;
	char* w5;
	int p = 0;
	int j;
	int a0 = NULL;

	// Wyznaczanie size
	w1 = strchr(a, '^');
	while (w1 != NULL)
	{
		if (atoi(&a[w1 - a + 1]) > p)
		{
			p = atoi(&a[w1 - a + 1]);
		}
		w1 = strchr(w1 + 1, '^');
	}
	if (strchr(a, '^') == NULL)
	{
		if (strchr(a, 'x') != NULL)
		{
			p = 1;
		}
	}
	
	size = p+1;
	wsp = new int[size]();

	// Wyznaczanie wspó³czynników przy potêgach
	w1 = strchr(a, '^');

	while (w1 != NULL)
	{
		j = 0;
		while (a[w1 - a - j] != '+' && a[w1 - a - j] != '-' && w1 - a - j != 0)
		{
			j++;
		}
		wsp[atoi(&a[w1 - a + 1])] = atoi(&a[w1 - a - j]);
		if (a[w1 - a - 2] == '+' || (w1 - a - 1 == 0 && a[w1 - a - 1] == 'x'))
		{
			wsp[atoi(&a[w1 - a + 1])] = 1;
		}
		else if (a[w1 - a - 2] == '-')
		{
			wsp[atoi(&a[w1 - a + 1])] = -1;
		}
		w1 = strchr(w1 + 1, '^');
	}

	// wyznaczanie wsp[1]
	w2 = strchr(a, 'x');
	while (w2 != NULL)
	{
		if (a[w2 - a + 1] != '^')
		{
			j = 0;
			while (a[w2 - a - j] != '+' && a[w2 - a - j] != '-' && w2 - a - j != 0)
			{
				j++;
			}
			wsp[1] = atoi(&a[w2 - a - j]);
			if (a[w2 - a - 1] == '+' || (w2 - a == 0 && a[w2 - a] == 'x'))
			{
				wsp[1] = 1;
			}
			else if (a[w2 - a - 1] == '-')
			{
				wsp[1] = -1;
			}
		}
		w2 = strchr(w2 + 1, 'x');
	}

	// wyznaczanie wsp[0]
	if (p == 0)
	{
		a0 = atoi(&a[0]);
	}

	w3 = strchr(a, '+');
	while (w3 != NULL && a0 == NULL)
	{
		j = 1;
		while ((int)a[w3 - a - j] >= 48 && (int)a[w3 - a - j] <= 57 && w3 - a - j != 0)
		{
			j++;
		}
		if (a[w3 - a - j] == '+' || a[w3 - a - j] == '-' || w3 - a - j == 0)
		{
			a0 = atoi(&a[w3 - a - j]);
		}
		w3 = strchr(w3 + 1, '+');
	}

	w4 = strchr(a, '-');
	while (w4 != NULL && a0 == NULL)
	{
		j = 1;
		while ((int)a[w4 - a - j] >= 48 && (int)a[w4 - a - j] <= 57 && w4 - a - j != 0)
		{
			j++;
		}
		if (a[w4 - a - j] == '+' || a[w4 - a - j] == '-' || w4 - a - j == 0)
		{
			a0 = atoi(&a[w4 - a - j]);
		}
		w4 = strchr(w4 + 1, '-');
	}

	w5 = strchr(a, '\0');
	while (a0 == NULL)
	{
		j = 1;
		while ((int)a[w5 - a - j] >= 48 && (int)a[w5 - a - j] <= 57)
		{
			j++;
		}
		if (a[w5 - a - j] == '+' || a[w5 - a - j] == '-' || w5 - a - j == 0)
		{
			a0 = atoi(&a[w5 - a - j]);
		}
	}
	if (a0 != NULL)
	{
		wsp[0] = a0;
	}

	if (p == 0)
	{
		wsp[0] = atoi(&a[0]);
	}
	
}

// DESTRUKTOR
wiel::~wiel()
{
	delete[] wsp;
}

// OPERATORY
wiel& wiel::operator=(const wiel& y)
{
	delete[] wsp;

	wsp = new int[y.size];
	size = y.size;
	memcpy(wsp, y.wsp, sizeof(int) * size);

	return *this;
}  

wiel wiel::operator+(const wiel& y)
{
	int s, b;
	int* tab;
	int* tmp;
	if (size > y.size)
	{
		s = size;
		tmp = wsp;
		b = 0;		
	}
	else
	{
		s = y.size;
		tmp = y.wsp;
		b = 1;		
	}
	tab = new int[s];
	memcpy(tab, tmp, sizeof(int) * s);
	if (b == 0)
	{
		for (int i = y.size - 1; i >= 0; i--)
		{
			tab[i] += y.wsp[i];
		}
	}
	else
	{
		for (int i = size - 1; i >= 0; i--)
		{
			tab[i] += wsp[i];
		}
	}

	wiel k(tab, s);
	delete[] tab;
	return k;
}
wiel wiel::operator+(int y)
{
	wiel w(*this);
	w.wsp[0] += y;
	return w;
}
wiel operator+(int y, const wiel& x)
{
	wiel w(x.wsp, x.size);
	w.wsp[0] += y;
	return w;
}
wiel& wiel::operator+=(const wiel& y)
{	
	int b, s;
	int* tab;
	int* tmp;
	if (size > y.size)
	{	
		s = size;
		tmp = wsp;
		b = 0;
	}
	else
	{
		s = y.size;
		tmp = y.wsp;
		b = 1;
	}
	tab = new int[s];
	memcpy(tab, tmp, sizeof(int) * s);
	if (b == 0)
	{
		for (int i = y.size - 1; i >= 0; i--)
		{
			tab[i] += y.wsp[i];
		}
	}
	else
	{
		for (int i = size - 1; i >= 0; i--)
		{
			tab[i] += wsp[i];
		}
	}
	size = s;
	wsp = tab;
	return *this;
}
wiel& wiel::operator+=(int y)
{
	wsp[0] += y;
	return *this;
}

wiel wiel::operator-(const wiel& y)
{
	int s, b;
	int* tab;
	int* tmp;
	if (size > y.size)
	{
		s = size;
		b = 0;
	}
	else
	{
		s = y.size;
		b = 1;
	}
	tab = new int[s];
	for (int i = s - 1; i >= 0; i--)
	{
		tab[i] = 0;
	}
	for (int i = size - 1; i >= 0; i--)
	{
		tab[i] += wsp[i];
	}
	for (int i = y.size - 1; i >= 0; i--)
	{
		tab[i] -= y.wsp[i];
	}
	wiel k(tab, s);
	delete[] tab;
	return k;
}
wiel wiel::operator-(int y)
{
	wiel w(*this);
	w.wsp[0] -= y;
	return w;
}
wiel operator-(int y, const wiel& x)
{
	wiel w(x.wsp, x.size);
	w.wsp[0] = -w.wsp[0] + y;
	for (int i = w.size - 1; i > 0; i--)
	{
		w.wsp[i] = -w.wsp[i];
	}
	return w;
}
wiel& wiel::operator-=(const wiel& y)
{
	int s, b;
	int* tab;
	int* tmp;
	if (size > y.size)
	{
		s = size;
		b = 0;
	}
	else
	{
		s = y.size;
		b = 1;
	}
	tab = new int[s];
	for (int i = s - 1; i >= 0; i--)
	{
		tab[i] = 0;
	}
	for (int i = size - 1; i >= 0; i--)
	{
		tab[i] += wsp[i];
	}
	for (int i = y.size - 1; i >= 0; i--)
	{
		tab[i] -= y.wsp[i];
	}
	size = s;
	wsp = tab;
	return *this;
}
wiel& wiel::operator-=(int y)
{
	wsp[0] -= y;
	return *this;
}

wiel wiel::operator*(const wiel& y)
{
	int z;
	int* tab;
	z = size + y.size - 1;
	tab = new int[z];

	for (int i = z - 1; i >= 0; i--)
	{
		tab[i] = 0;
	}

	for (int i = size - 1; i >= 0; i--)
	{
		for (int j = y.size - 1; j >= 0; j--)
		{
			tab[i + j] += wsp[i] * y.wsp[j];
		}
	}

	wiel k(tab, z);
	return k;
}
wiel wiel::operator*(int y)
{
	wiel w(*this);
	for (int i = size - 1; i >= 0; i--)
	{
		w.wsp[i] *= y;
	}
	return w;
}
wiel operator*(int y, const wiel& x)
{
	wiel w(x.wsp, x.size);
	for (int i = x.size - 1; i >= 0; i--)
	{
		w.wsp[i] *= y;
	}
	return w;
}
wiel& wiel::operator*=(const wiel& y)
{
	int z;
	int* tab;
	z = size + y.size - 1;
	tab = new int[z];

	for (int i = z - 1; i >= 0; i--)
	{
		tab[i] = 0;
	}

	for (int i = size - 1; i >= 0; i--)
	{
		for (int j = y.size - 1; j >= 0; j--)
		{
			tab[i + j] += wsp[i] * y.wsp[j];
		}
	}

	wsp = tab;
	size = z;
	return *this;
}
wiel& wiel::operator*=(int y)
{
	for (int i = size - 1; i >= 0; i--)
	{
		wsp[i] *= y;
	}
	return *this;
}

ostream& operator<<(ostream& o, const wiel& y)
{
	int b = 0;
	for (int i = y.size - 1; i >= 0; i--)
	{
		if (y.wsp[i] != 0)
		{
			if (y.wsp[i] < 0)
			{
				o << "-";
			}
			else
			{
				o << "";
			}

			if (abs(y.wsp[i]) == 1)
			{
				o << "";
			}
			else
			{
				o << abs(y.wsp[i]);
			}

			if (i == 0)
			{
				cout << "";
				if (abs(y.wsp[i]) == 1)
				{
					o << abs(y.wsp[i]);
				}
			}
			else if (i == 1)
			{
				o << "x";
			}
			else
			{
				o << "x^" << i;
			}
		}

		if (y.wsp[i - 1] <= 0)
		{
			o << "";
		}
		else
		{
			o << "+";
		}
	
		if (y.wsp[i] != 0)
		{
			b = 1;
		}		
	}
	if (b == 0)
	{
		o << 0;
	}

	return o;
}

// METODY
wiel* wiel::Add(wiel* y)
{
	wiel w(this->wsp, this->size);
	wiel v(y->wsp, y->size);
	wiel z;
	z = w + v;

	wiel* m = new wiel(z.wsp, z.size);
	return m;
}

void wiel::Wyswietl()
{
	cout << *this;
}
