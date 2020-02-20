//
// Created by 徐维亚 on 20/02/2020.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    void moveZeroes1(vector<int> &nums) {
        int p = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[p] = nums[i];
                p++;
            }
        }
        while (p < nums.size()) {
            nums[p] = 0;
            p++;
        }
    }

// Traverse only once by using swap.
    void moveZeros2(vector<int> &nums) {
        int p = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                swap(nums[p++], nums[i]);
            }
        }
    }
};

int main(void) {
    Solution s;
    vector<int> nums({0,1,0,3,12});

    cout << "Before: ";
    for(auto v: nums){
        cout << v << " ";
    }
    cout << endl;

    s.moveZeroes1(nums);

    cout << "After: ";
    for(auto v: nums){
        cout << v << " ";
    }
    cout << endl;

}