class Solution:
    def twoSum(self, nums, target):
        list_index = ([(num, index) for index, num in enumerate(nums)])
        list_index.sort()
        start, end = 0, len(list_index) - 1
        while start < end:
            check_target = list_index[start][0] + list_index[end][0]
            if check_target == target:
                return [list_index[start][1] + list_index[end][1]]
            if check_target < target:
                start += 1
            else:
                end -= 1
