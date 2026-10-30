class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        my_list = nums1 + nums2
        my_list.sort()

        n = len(my_list)

        if n % 2 == 1:
            median = my_list[n // 2]
        else:
            median = (my_list[n // 2 - 1] + my_list[n // 2]) / 2

        return median