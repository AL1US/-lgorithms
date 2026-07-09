from typing import List

# O(n в кварате) - худшее, что может быть
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] == nums[right]:
                return True
                break
            else:
                if right != left + 1:
                    right -= 1
                else:
                    left += 1
                    right = len(nums) - 1
        return False

# O(n) - хеш таблица)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()
        for i in nums:
            if i in hash_table:
                return True
            else:
                hash_table.add(i)
                
        return False
    
class Solution: # Обычная сортировка и указатели
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return True
            else:
                slow += 1
                fast += 1
                        
        return False