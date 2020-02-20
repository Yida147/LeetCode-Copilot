//
// Created by 徐维亚 on 20/02/2020.
//

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
//    维护从左到右、从右到左的acceding队列，得到第i个位置左右两边最高的数值
    int trap1(vector<int>& height) {
        int * max_l = new int[height.size()];
        int * max_r = new int[height.size()];

        int m1 = 0, m2 = 0;
        for(int i = 0; i < height.size(); i++) {
            max_l[i] = m1;
            max_r[height.size()-1-i] = m2;

            m1 = max(m1, height[i]);
            m2 = max(m2, height[height.size()-1-i]);
        }
        int res = 0;
        for(int i = 0; i < height.size(); i++) {
            res += max(0, min(max_l[i], max_r[i]) - height[i]);
        }
        delete [] max_l;
        delete [] max_r;
        return res;
    }

//    左右夹逼，without extra space
    int trap2(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int l_max = 0, r_max = 0;
        int res = 0;
        while (l <= r) {
            if (l_max <= r_max) {
                res += max(0, l_max - height[l]);
                l_max = max(l_max, height[l]);
                l++;
            } else {
                res += max(0, r_max - height[r]);
                r_max = max(r_max, height[r]);
                r--;
            }
        }
        return res;
    }
};

int main(void) {
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};

    int res = 0;
    Solution s;
    res = s.trap2(height);
    cout << "Output: " << res << endl;
    return 0;
}