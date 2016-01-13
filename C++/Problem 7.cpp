// By Allister Moon, September 2014
/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
*/
// Answer: 104743
// Time: 0.775 seconds
#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(long long num) {

    for(long long i = 2; i <= sqrt(num); i++) {
        if(num % i == 0) return false;
    }
    return true;
}

int main() {

    int desiredPrime = 10001;
    int primeCount = 1;
    long long currentPrime = 2;

    long long i = 3;
    while(primeCount != desiredPrime) {
        if(isPrime(i)) {
            primeCount++;
            currentPrime = i;
        }
        i += 2;
    }

    cout << currentPrime << endl;
    return 0;
}

// Notes:
// I was worried about the brute force approach, but it does not seem too bad here.
