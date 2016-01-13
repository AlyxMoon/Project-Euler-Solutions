/* By Allister Moon, September 2014
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/
// Answer: 6857

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

    long long number = 600851475143;
    long long answer = number;

    for(long long i = 2; i <= sqrt(number); i++) {
        if(number % i == 0) {
            if(isPrime(number / i)) {
                answer = number / i;
                break;
            }
            else if(isPrime(i)) answer = i;
        }
    }

    cout << answer << endl;
    return 0;
}
