// By Allister Moon, September 2014
/*
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/
// Answer: 25164150
// Time: 0.191
#include <iostream>
using namespace std;

int GetSquareOfSums(int upperBounds) {
    int sum = 0;

    for(int i = 1; i <= upperBounds; i++) {
        sum += i;
    }
    sum *= sum;
    return sum;
}
int GetSumOfSquares(int upperBounds) {
    int sum = 0;

    for(int i = 1; i <= upperBounds; i++) {
        sum += (i * i);
    }
    return sum;
}


int main() {
    int upperBounds = 100;

    cout << GetSquareOfSums(upperBounds) - GetSumOfSquares(upperBounds)<< endl;
    return 0;
}


// Notes:
// Just simple calculation works very well, but I'm wondering if there is a mathematical shortcut.
// Eh, that's pretty simplified already, I haven't found anything concrete. It works and is good.
