// By Allister Moon, September 2014
/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/
// Answer: 142913828922
// Time: 0.383 seconds

#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

bool isPrime(long long num) {

    for(long long i = 2; i <= sqrt(num); i++) {
        if(num % i == 0) return false;
    }
    return true;
}

int main() {
/* Time: 35.878 seconds
    long long answer = 2;
    long long upperBound = 2000000;

    for(long long i = 3; i < upperBound; i += 2) {
        if(isPrime(i)) answer += i;
    }

    cout << answer << endl;
    return 0;
*/
    int upperBound = 2000000;
    int* sieve = new int[2000000];
    long long answer = 2;

    for(int i = 3; i < upperBound; i += 2) {
        if(sieve[i] == 0) {
            answer += i;

            int j = i;
            while(j < upperBound) {
                sieve[j] = 1;
                j += i;
            }
        }
    }

    cout << answer << endl;
    delete [] sieve;
    return 0;

}

// Notes:
// Have idea for better prime finder, using a linked list that remember previous primes to check against new numbers
// After all, if a number can be divided by something, it can be divided by a prime! It's a math thing!

// In practice, the very act of storing and adding to this list creates a HUGE time addition, well over 3 minutes at least.

// Used a normal array instead of dynamic vector, and after making sure I initialized it on the heap...it took a super short time!
