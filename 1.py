<<<<<<< HEAD
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i,j]

nums = [2, 7, 11, 15]
target = 9

#::
=======
#sum of two numbers
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i,j]

nums = [2, 7, 11, 15]
target = 9

>>>>>>> a8bce7b279560dbfcd6092f39590dff63ebc36d6
