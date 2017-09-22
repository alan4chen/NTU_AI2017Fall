import random

from hw0_r06922048.task1 import twoSum

if __name__ == "__main__":
    #Simple Test
    nums  = [2, 7, 11, 15]
    ans = twoSum(nums, 17)
    print ans

    random.seed(1)

    #Test2
    lst = []
    for i in range(1000):
        lst.append(random.randint(1, 1000))
    lst[133] += 1000
    lst[733] += 1000
    ret = twoSum(lst, lst[133]+lst[733])
    assert ret[0] == 133 and ret[1] == 733

    # Test3
    lst = []
    for i in range(100000):
        lst.append(random.randint(1, 1000))
    lst[1333] -= 1000
    lst[7333] -= 1000
    ret = twoSum(lst, lst[1333] + lst[7333])
    assert ret[0] == 1333 and ret[1] == 7333

