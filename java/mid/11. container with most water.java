class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right = height.length -1;
        int max_capacity=0;

        while (left<right){
           max_capacity = Math.max(max_capacity, (right - left) * Math.min(height[left], height[right]));
            if( height[left]>height[right]){
                right--;
            }
            else{
                left++;
            }
        }
        return  max_capacity;
    }
}