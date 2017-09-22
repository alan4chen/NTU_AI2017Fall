"""
    Created by Po-Yao Chen
    2017.9.11
"""



def twoSum(nums, target):

    map = dict()
    for index, val in enumerate(nums):
        map[val] = index
    for index, val in enumerate(nums):
        if target-val in map:
            return [index, map[target - val]]





