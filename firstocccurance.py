# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 12:09:16 2022

@author: Adagani
"""

def findfirstOccurrence(nums, target):

    (left, right) = (0, len(nums) - 1)
 
    result = -1
 
 
    while left <= right:
 
       
        mid = (left + right) // 2
 
   
        if target == nums[mid]:
            result = mid
            left = mid + 1
 
        elif target < nums[mid]:
            right = mid - 1
 
       
        else:
            left = mid + 1
 
   
    return result
 
 
if __name__ == '__main__':
 
    nums = [1,2,3,2,1]
    target = 2
 
    index = findfirstOccurrence(nums, target)
 
    if index != -1:
        print(f'The first occurrence of element {target} ')
    else:
        print('Element found not in the list')
 


