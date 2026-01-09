class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] a=new int[nums.length];
        a[0]=1;
  
        for (int i=1;i<nums.length;i++){
            a[i]=a[i-1]*nums[i-1];
        }
        int ri=1;
        for(int j=nums.length -1;j>=0;j--){
            a[j]*=ri;
            ri*=nums[j];
        }
        return a;
    }
}