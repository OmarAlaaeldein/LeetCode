class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zeros=0;
        int ones=0;
        int twos=0;
        for (int i=0;i<nums.size();i++){
            if (nums[i]==0){
                zeros+=1;
            }
            else if (nums[i]==1){
                ones+=1;
            }
            else{
                twos+=1;
            }
        }
        for (int i=0;i<nums.size();i++){
            if (zeros!=0){
                zeros-=1;
                nums[i]=0;
            } // done with zeros
            else if (ones!=0){
                ones-=1;
                nums[i]=1;
            }
            else{
                twos-=1;
                nums[i]=2;
            }
        }
    }
};