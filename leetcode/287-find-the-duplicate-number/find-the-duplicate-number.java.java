public class Solution {
    public int findDuplicate(int[] nums) {
        int[] temp =nums;
        Arrays.sort(temp);
        for(int i=1;i<temp.length;i++){
            if(temp[i]==temp[i-1])
                return temp[i];
        }
        return 0;
    }
}

