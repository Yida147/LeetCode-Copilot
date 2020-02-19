public class LeetCode_11_541 {
    // 一维数组的遍历
    // 枚举 面积  (x - y) * height_diff（短板效应导致只能取高度最小值）
    public int containerWithMostWaterSolution1(int [] height) {
        int max = 0;
        for ( int i = 0; i < height.length -1; ++i ) {
            for ( int j = i +1; j < height.length; ++j) {
                int area = ( j -i ) * Math.min( height[i], height[j] );
                max = Math.max(max, area);
            }
        }
        return max;
    }

    // 头指针 + 尾指针遍历
    public int containerWithMostWaterSolution2(int [] height) {
        int max = 0;
        for (int i = 0, j = height.length -1; i < j; ) {
            int minHeight = height[i] < height[j] ? height[ i++ ] : height[ j-- ];
            max = Math.max( max, (j - i + 1) * minHeight );
        }
        return max;
    }

    public static void main(String[] args) {
        int [] height = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
        LeetCode_11_541 agent = new LeetCode_11_541();
//        int result = agent.containerWithMostWaterSolution1(height);
        int result = agent.containerWithMostWaterSolution2(height);
        System.out.println(result);
    }
}
