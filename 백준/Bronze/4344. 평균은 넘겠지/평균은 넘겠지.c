#include <stdio.h>
#define MAX 1000

int main() {
    int c;
    scanf("%d", &c);
    for (int i = 0; i < c; i++) {
        int n, sum = 0, x = 0;
        int stu[MAX];
        scanf("%d", &n);
        for (int j = 0; j < n; j++) {
            scanf("%d", &stu[j]);
            sum = sum + stu[j];
        }
        float ave = (float) sum / n;
        for (int k = 0; k < n; k++) {
            if (stu[k] > ave) {
                x++;
            }
        }
        float y = ((float)x / n) * 100;
        printf("%.3f%%\n", y);
    }
    return 0;
}