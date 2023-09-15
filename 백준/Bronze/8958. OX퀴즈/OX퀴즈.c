#include <stdio.h>
#include <string.h>
#define MAX 80

int main() {
    int n;
    scanf("%d", &n);
    char a[MAX];
    for (int i = 0; i < n; i++) {
        int x = 0, sum = 0;
        scanf("%s", a);
        int len = strlen(a);
        for (int j = 0; j < len; j++) {
            if (a[j] == 'O') {
                x++;
                sum = sum + x;
            }
            else if (a[j] == 'X') {
                x = 0;
            }
            else break;
         }
        printf("%d\n", sum);
     }
    return 0;
}