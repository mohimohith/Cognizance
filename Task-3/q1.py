import numpy as np
lst=input("enter the array numbers with gap : ").split()
nums = np.array(lst)
nums=[int(i) for i in nums]
print("Original array:")
print(nums)
new_nums = np.zeros(len(nums) + (len(nums)-1)*(5))
new_nums[::5+1] = nums
print("\nNew array:")
print(new_nums)