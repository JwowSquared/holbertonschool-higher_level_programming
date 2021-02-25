#!/usr/bin/python3
"""x"""


def find_peak(nums):
    """x"""
    if nums is None or len(nums) is 0:
        return None

    nums.append(None)
    up = True
    prev = nums[0]
    for i in range(1, len(nums)):
        if up and (nums[i] is None or prev > nums[i]):
            return prev
        prev = nums[i]

    return None
