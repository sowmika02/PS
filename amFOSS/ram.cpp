#include <map>
#include <iostream>
using namespace std;

#define long long long
const long M = 1000000007;
map<long, long> F;

long f(long n) {
	if (F.count(n)) return F[n];
	long k=n/2;
	if (n%2==0) {
		return F[n] = (f(k)*f(k) + f(k-1)*f(k-1)) % M;
	} else {
		return F[n] = (f(k)*f(k+1) + f(k-1)*f(k)) % M;
	}
}

int main(){
	long n;
	int a, b, c, d, l;
	cin>>l;
	cin>>a>>b>>c>>d>>n;
	for (int i=0; i<l; i++){
		F[0]=a;
		F[1]=b;
		cout << f(n-1)<< endl;
	}
}