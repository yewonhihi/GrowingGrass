#include <stdio.h>
#define MAX 1000

int main() {
    int n;
    float max = 0, count = 0;
    float a[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%f", &a[i]);
        if (a[i] > max) {
            max = a[i];
        }
    }
    for (int i = 0; i < n; i++) {
        a[i] = (a[i] / max) * 100;
        count = count + a[i];
    }
    printf("%f", count / n);
    return 0;
}