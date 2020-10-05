#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n,c,i;
    cin>>n;
    c=0;
    for (i=1;i<=sqrt(n);i++){ 
        if(n%i==0){ 
            c=c+2;
            if(i==sqrt(n)){
                c--;
            }
        } 
    } 
    cout<<c<<endl;
}