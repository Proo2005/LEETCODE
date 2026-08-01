class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[]{-1, -1};

        result[0] = findBoundary(nums, target, true);
        
        
        if (result[0] != -1) {
            result[1] = findBoundary(nums, target, false);
        }
        
        return result;
    }
    
    private int findBoundary(int[] nums, int target, boolean isFirst) {
        int left = 0;
        int right = nums.length - 1;
        int index = -1;
        
        while (left <= right) {

            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                index = mid; 
                
                if (isFirst) {
                    right = mid - 1; 
                } else {
                    left = mid + 1;  
                }
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return index;
    }
}
