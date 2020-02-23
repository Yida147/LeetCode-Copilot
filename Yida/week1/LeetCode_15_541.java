import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode_15_541 {
    public ArrayList<java.util.List<Integer>> threeSumSolution1(int[] nums) {
        ArrayList<java.util.List<Integer>> ans = new ArrayList<>();
        int len = nums.length;
        if (len < 3) return ans;
        Arrays.sort(nums);
        for ( int i = 0; i < len; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums [i -1]) continue;
            int L = i + 1;
            int R = len - 1;
            while ( L < R ) {
                int sum = nums[i] + nums[L] + nums[R];
                if (sum == 0) {
                    ans.add(Arrays.asList(nums[i], nums[L], nums[R]));
                    while ( L < R && nums[L] == nums[L+1]) L++;
                    while ( L < R && nums[R] == nums[R-1]) R--;
                    L++;
                    R--;
                }
            }
        }
        return ans;
    }

    public List<List<Integer>> threeSumSolution2(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i + 2 < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int j = i + 1, k = nums.length - 1;
            int target = -nums[i];
            while (j < k) {
                if (nums[j] + nums[k] == target) {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                    while (j < k && nums[j] == nums[j - 1]) j++;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                } else if (nums[j] + nums[k] > target) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        return res;
    }
}
