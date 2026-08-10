#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    vector<string> ans;
    void solve(string& current, int open, int close, int n) {
        if (current.length() == 2 * n) {
            ans.push_back(current);
            return;
        }
        if (open < n) {
            current.push_back('(');
            solve(current, open + 1, close, n);
            current.pop_back();
        }
        if (close < open) {
            current.push_back(')');
            solve(current, open, close + 1, n);
            current.pop_back();
        }
    }
    vector<string> generateParentheses(int n) {
        string current = "";
        solve(current, 0, 0, n);
        return ans;
    }
};
int main() {
    Solution solver;
    int n = 3;  
    vector<string> result = solver.generateParentheses(n);
    cout << "Generated Parentheses for n" << n << ":" << endl;
    for (const string& s : result) {
        cout << s << endl;
    }
    return 0;
}
