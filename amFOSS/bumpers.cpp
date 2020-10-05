#include <iostream>
using namespace std;

int main() {
    int a, b, n;
    cin >> n;
    cin >> a >> b;
    for (int i=0; i<n; i++) {
        int count =0;
        while (true){
            if (a != b){
                if (a < b){
                    if (b - a < 11){
                        count = count + 1;
                        break;
                    }
                    else{
                        a = a + 10;
                        count = count + 1;
                    }
                }
                else{
                    if (a - b < 11){
                        count = count + 1;
                        break;
                    }
                    else{
                        b = b + 10;
                        count = count + 1;
                    }
                }
            }
            else{
                break;
            }
        }
        cout << count << endl;
    }
    return 0;
}
