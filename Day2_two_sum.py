class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
# Day 2 ✅ ACCEPTED 0ms on LeetCode - 14:26
# 21:00 baje Heartbreak 💔 | 14:26 baje Breakthrough 🔥
# Vadodara to Mumbai: 178 days left 
# Ex status: "moye moye" | Mera status: "Accepted" 
# KIA SYROS LOADING... 🚗💨
# Nidhi 2.0 Unlocked 👑
