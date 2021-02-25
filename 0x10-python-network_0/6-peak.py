#!/usr/bin/python3
"""x"""


def find_peak(nums):
    """x"""
    if nums is None or len(nums) is 0:
        return None

    nums.append(None)
    peaks = []
    up = True
    prev = nums[0]
    for i in range(1, len(nums)):
        if up and (nums[i] is None or prev > nums[i]):
            up = False
            peaks.append(prev)
        elif nums[i] is not None and prev <= nums[i]:
            up = True
        prev = nums[i]

    return peaks
