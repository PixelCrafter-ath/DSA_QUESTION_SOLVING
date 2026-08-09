#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<vector<int>> ans;
void solve(int start, vector<int>& candidates, int target, vector<int>& current) {
    if (target == 0) {
        ans.push_back(current);
        return;
    }
        for (int i = start; i < candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
            continue;
            }
            if (candidates[i] > target) {
            break;
            }
        current.push_back(candidates[i]);
        solve(i + 1, candidates, target - candidates[i], current);
        current.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    ans.clear();
    sort(candidates.begin(), candidates.end());
    vector<int> current;
    solve(0, candidates, target, current);
    return ans;
}

int main() {
    vector<int> candidates = {10, 1, 2, 7, 6, 1, 5};
    int target = 8;
    vector<vector<int>> result = combinationSum2(candidates, target);
    for (vector<int> combination : result) {
        cout << "{";
        for (int x : combination) {
            cout << x << " ";
        }
        cout << "}" << endl;
    }
    return 0;
}
