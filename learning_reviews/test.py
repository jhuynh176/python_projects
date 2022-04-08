import enum


nums = [9,8,7,6,5,4,3,2,1]

for i, num in enumerate(nums):
    print(i, num)
    for j, val in enumerate(nums[i:]):
        print('\t',j+i,val)