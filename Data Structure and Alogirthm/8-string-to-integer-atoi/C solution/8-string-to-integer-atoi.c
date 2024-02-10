#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h> // Include for pow()

int myAtoi(char* s) {
    // Handle edge case of empty string
    if (strlen(s) == 0) {
        return 0;
    }

    long long total = 0; // Use long long to handle larger numbers
    int sign = 1;

    // Skip leading spaces
    int i = 0;
    while (s[i] == ' ') {
        i++;
    }

    // Check for sign
    if (s[i] == '+' || s[i] == '-') {
        sign = (s[i] == '+') ? 1 : -1;
        i++;
    }

    // Convert digits to number, handle overflow/underflow
    while (s[i] >= '0' && s[i] <= '9') {
        long long next_total = total * 10 + (s[i] - '0');
        // Check for overflow/underflow before adding
        if (sign == 1 && next_total > INT_MAX || sign == -1 && next_total < INT_MIN) {
            return sign == 1 ? INT_MAX : INT_MIN;
        }
        total = next_total;
        i++;
    }

    return total * sign;
}
