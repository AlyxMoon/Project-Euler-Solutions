// By Allister Moon, September 2014
/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c2^

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/
// Answer: 31875000
// Time: 0.323 seconds
#include <iostream>
#include <math.h>
using namespace std;

int main() {

    int tripletA = 0, tripletB = 0, tripletC = 0;
    int answer = 0;

    bool tripletFound = false;
    for(int c = 5; c <= 1000; c++) {

        for(int b = 3; b < c; b++) {

            for(int a = 2; a < b; a++) {

                if( (a*a + b*b) == (c*c) ) {
                    if(a + b + c == 1000) {
                        tripletA = a;
                        tripletB = b;
                        tripletC = c;
                        answer = a * b * c;
                        tripletFound = true;
                        break;
                    }
                }
            }
            if(tripletFound) break;
        }
        if(tripletFound) break;
    }

    cout << tripletA << ", " << tripletB << ", " << tripletC << endl;
    cout << answer << endl;
    return 0;
}
