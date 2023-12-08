#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0,r=height.size()-1;
        int maxS=0;
        while(l<r){
            int area = min(height[l], height[r]) * (r - l);
            maxS=max(area,maxS);
            if (height[l]<height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxS;
    }
};

int main(){
    Solution s=Solution();
    vector<int> v={1,8,6,2,5,4,8,3,7};
    cout << s.maxArea(v) << endl;
}