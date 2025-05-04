#include <bits/stdc++.h>
using namespace std;
typedef vector<vector<pair<int,int>>> vvpr;

vvpr graph(){
    int vertices, edges;
    cin >> vertices >> edges;
    vvpr adjacent_list(vertices, vector<pair<int,int>>());
}



int main(){
    vvpr adjacent_list = graph();
    int source = 0;
    cin >> source;
    vector<int> distance = shortest_distance(adjacent_list, source);
    for (int i: distance){
        cout << i << " ";
    }
    return 0;
}