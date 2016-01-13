/* By Allister Moon, September 2014
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/
// Answer: 906609

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

bool isPalindrome(int num) {
    char tempChar1, tempChar2;
    stringstream ss;
    ss << num;
    string tempString = ss.str();
    int l = tempString.length() - 1;
    for(int j = 0; j <= l / 2; j++) {
        tempChar1 = tempString.at(j);
        tempChar2 = tempString.at(l - j);
        if(tempChar1 != tempChar2) return false;
    }
    return true;
}

int main() {

    int bounds = 999 * 999;
    int answer = 0;

    for(int i = 100; i <= 999; i++) {
        for(int j = 100; j <= 999; j++) {
            int tempNum = i * j;
            if(isPalindrome(tempNum) && answer < tempNum) {
                answer = tempNum;
            }
        }
    }

    cout << answer << endl;
    return 0;
}
