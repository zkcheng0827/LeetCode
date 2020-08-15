class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
    /*
    448. Find All Numbers Disappeared in an Array
    64%
    */
        for(int i = 0; i < nums.size(); i++)
        {
            while(nums[i] <= nums.size() && nums[i] != nums[nums[i] - 1])
            {
                int tmp = nums[i];
                nums[i] = nums[tmp - 1];
                nums[tmp - 1] = tmp;
            }
        }
        vector<int> missing;
        for(int i = 0; i < nums.size(); i++)
            if(nums[i] != i + 1)
                missing.push_back(i+1);
        return missing;
    }
};
