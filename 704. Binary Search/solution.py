class Solution:
    def search(self, nums: list, target: int) -> int:
        if len(nums):
            m = int(len(nums)/2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return self.search(nums[:m], target)
            elif nums[m] > target:
                return self.search(nums[m:], target)
        else:
            return -1

if __name__ == '__main__':
    a = Solution().search([-1,0,3,5,9,12], 9)
    print(a)