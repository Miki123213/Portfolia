#pragma once

#include <iostream>
#include <string>

using namespace std;

class wiel
{
	int* wsp;
	int size;
public:
	
	wiel();
	wiel(int*, int);
	wiel(wiel&);
	wiel(char*);
	~wiel();

	wiel& operator=(const wiel&);						// wiel = wiel

	wiel operator+(const wiel&);						// wiel + wiel
	wiel operator+(int);								// wiel + int
	friend wiel operator+(int, const wiel&);			// int + wiel
	wiel& operator+=(const wiel&);						// wiel += wiel
	wiel& operator+=(int);								// wiel += int

	wiel operator-(const wiel&);						// wiel - wiel
	wiel operator-(int);								// wiel - int
	friend wiel operator-(int, const wiel&);			// int - wiel
	wiel& operator-=(const wiel&);						// wiel -= wiel
	wiel& operator-=(int);								// wiel -= int

	wiel operator*(const wiel&);						// wiel * wiel
	wiel operator*(int);								// wiel * int
	friend wiel operator*(int, const wiel&);			// int * wiel
	wiel& operator*=(const wiel&);						// wiel *= wiel
	wiel& operator*=(int);								// wiel *= int

	friend ostream& operator<<(ostream&, const wiel&);	// << wiel

	wiel* Add(wiel*);
	void Wyswietl(); 
};