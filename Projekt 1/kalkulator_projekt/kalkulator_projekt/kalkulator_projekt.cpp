// kalkulator_projekt.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//

#include <iostream>
#include <string>
using namespace std;

float power(float a, int b) {
	if (b == 0) return 1;
	else if (b < 0) return pow(1 / a, -b);
	return power(a, b - 1)* a;
}


string calculate(float a, float b, char operant) {
	if (!a || !b || !operant) {
		return "error: incorrect input!";
	}
	switch (operant)
	{
	case '+':
		return to_string(a + b);
		break;

	case '-':
		return to_string(a - b);
		break;

	case '*':
		return to_string(a * b);
		break;

	case '/':
		return to_string(a / b);
		break;

	case '^':
		return to_string(power(a, (int)b));
		break;

	case '%':
		return to_string((int)a % (int)b);
		break;

	default:
		break;
	}
}



int main()
{
	
	cout << "Simple Calculator V1.0\n";
	cout << "Simply type a + b witout quotes and hit enter\n";
	cout << "Use comma '.' decimal ex. 3.14; Available operantors: + - * / ^ % \n";
	cout << "------------------------------------\n";
	while (true) {
		float a, b;
		char oper;
		cout << ">>";
		cin >> a >> oper >> b;
		cout << "output: " << calculate(a, b, oper) << "\n";
	}

}
