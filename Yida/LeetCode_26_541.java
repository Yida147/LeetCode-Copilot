/**
 * Given sorted array nums = [1,1,2],
 *
 * Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
 *
 * It doesn't matter what you leave beyond the returned length.
 * @since 1.8
 */

public class LeetCode_26_541 {
    // 排序后数组，使用快慢双指针把不重复元素移到数组左边 时间复杂度O(n), 空间复杂度O(1)
    public int removeDuplicatesSolution1(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int p = 0;
        int q = 1;
        while ( q < nums.length ) {
            if (nums[p] != nums[q]){
                nums[p+1] = nums[q];
                p++;
            }
            q++;
        }
        return p + 1;
    }
}
