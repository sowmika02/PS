#include<iostream>
using namespace std;

int main (void){
    int q,k, a;
    long long n;

    scanf ("%d",&q);

    while (q--){
        scanf ("%lld",&n);
        k = 0;
        while (n > 1){
            if (n % 2 == 0)
                n /= 2;
            else if (n % 3 == 0){
                n /= 3;
                n *= 2;
            }
            else if (n % 5 == 0){
                n /= 5;
                n *= 4;
            }
            else{
                k = -1;
                break;
            }
            k++;
        }
        printf ("%d\n",k);
    }
    return 0;
}
