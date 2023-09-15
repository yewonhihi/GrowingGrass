#include <stdio.h>

int main() {
    int n;
    int i = 0;
    scanf("%d", &n);
    int x = n;
    while (1) {
        int a = x / 10;
        int b = x % 10;
        int c = (a + b) % 10;
        x = 10 * b + c;
        i = i + 1;
        if (n == x) {
            printf("%d", i);
            break;
        }
    }
    return 0;
}