#include <bits/stdc++.h>
using namespace std;

int main() {
    int x, n, a, b, c;
    cout << "Array elements: ";
    cin >> x;
    bool hasFirst = false;
    bool hasSecond = false;
    bool hasThird = false;
    int numbers[x];
    for(int i = 0; i < x; i++){
        cin >> n;
        numbers[i] = n;
    }
    for(int i = 0; i < x; i++){
        n = numbers[i];
        if(!hasFirst){
            a = n;
            hasFirst = true;
        }
        else if(a < n){
            if(hasSecond){
                c = b; 
                hasThird = true;
            }
            
            b = a;
            hasSecond = true;

            a = n;
        }
        else if(n < a && (!hasSecond || n > b)){
            if(hasSecond){
               c = b;
                hasThird = true;
            }
            
            b = n;
            hasSecond = true;
        }
        else if(n < b && (!hasThird || n > c)){
            c = n;
            hasThird = true;
        }
    }
    if(hasThird){
        cout << c;
    }
    else{
        cout << "No third-largest distinct element";
    }
    return 0;
}
