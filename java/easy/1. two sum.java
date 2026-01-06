class Solution {
    public int[] twoSum(int[] nums, int target) {
        int a = 0, b = 0;

        for (int i = 0; i < nums.length; i++) {
            a = nums[i];

            for (int j = 0; j < nums.length; j++) {
                b = nums[j];

                if (i != j && a + b == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}
