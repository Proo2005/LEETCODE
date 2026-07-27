import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] > nums[j]) {
                    int temp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = temp;
                }
            }
        }
        
        int left = 0;
        int right = nums.length - 1;

        for (int i = 0; i < nums.length; i++) {
     
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int a = nums[i];
            left = i + 1;
            right = nums.length - 1;

            while (left < right) {
                int currentSum = a + nums[left] + nums[right];
                
                if (currentSum == 0) {
                    arr.add(Arrays.asList(a, nums[left], nums[right]));
                    
    
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
           
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
      
                    left++;
                    right--;
                } else {
                    if (currentSum > 0) {
                        right--;
                    }
                    if (currentSum < 0) {
                        left++; 
                    }
                }
            }
        }
        return arr;
    }
}
