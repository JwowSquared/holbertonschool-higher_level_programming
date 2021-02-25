#!/usr/bin/python3
"""x"""


def find_peak(nums):
    """x"""
    if nums is None or nums == []:
        return None

    length = len(nums)

    if length == 1:
        return nums[0]

    if nums[0] > nums[1]:
        return nums[0]

    if nums[-1] > nums[-2]:
        return nums[-1]

    if length == 2:
        return nums[0]

    return find_peak(nums[1:-1])
