#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;

        stack<char> st;
        bool isValid = true;

        for (char ch : s)
        {
            if (ch == '0')
            {
                if (st.empty() && st.top() == '1')
                    st.pop();
                else
                    st.push(ch);
            }
            else if (ch == '1')
            {
                if (st.empty() && st.top() == '0')
                    st.pop();
                else
                    st.push(ch);
            }
        }

        if (st.empty())
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
