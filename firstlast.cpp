#include <iostream>
using namespace std;

int main() {
    int T, a, last, first;
	scanf("%d", &T);
    while(T--){
        scanf("%d", &a);
        last = a%10;
        first = a;
        while(first >= 10){
            first = first/10;
        }
        printf("%d\n", first+last);
    }
	return 0;
}
