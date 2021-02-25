#!/usr/bin/python3
"""x"""


def find_peak(nums):
    """x"""
    if nums is None or nums == []:
        return None

    if len(nums) == 1:
        return nums[0]

    if nums[0] > nums[1]:
        return nums[0]

    if nums[-1] > nums[-2]:
        return nums[-1]

    return find_peak(nums[1:-1])
