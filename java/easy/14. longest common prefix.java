class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String left=strs[0];
        String right=strs[strs.length - 1];
        StringBuilder common = new StringBuilder();

        for (int i=0;i<Math.min(left.length(),right.length());i++){
            if (left.charAt(i)==right.charAt(i)){
                common.append(left.charAt(i));
            }
            else{
                break;
            }
        }
        return common.toString();
    }
}