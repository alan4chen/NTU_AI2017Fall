#!/usr/bin/python
# -*- coding: utf8 -*-

def twoSum(nums, target):
    numsDict = dict()
    for i in range(len(nums)):
        numsDict[nums[int(i)]] = int(i)
        
    for i in range(len(nums)):
        if (target-nums[int(i)]) in numsDict:
            return [i, numsDict[(target-nums[int(i)])]]
    
    
if __name__ == '__main__':
    nums = [2, 7, 2, 15]
    ans = twoSum(nums, 4)
    print ans
    