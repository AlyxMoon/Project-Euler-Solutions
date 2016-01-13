// By Allister Moon, September 2014
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/
// Answer: 232792560
// Time: 0.723 seconds
#include <iostream>
using namespace std;

int main() {

    long long answer = 0;
    long long numMax = 20;

    for(long long i = 20; i <= 1000000000; i += 20) {
        for(long long j = 11; j <= numMax; j++) {
            if(i % j != 0) break;

            if(j == numMax) answer = i;
        }
        if(answer != 0) break;
    }

    cout << answer << endl;
    return 0;
}

// Thoughts

// First 10 numbers are redundant, not needed in checks
// Can eliminate a lot of numbers for testing, has to be an even number, multiple of 20
// These two checks reduced time from 17.397 seconds to 0.723 seconds

