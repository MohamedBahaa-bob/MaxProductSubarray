# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def maxProductNoZeros(temp, even) -> int:
    if len(temp) == 0:
        return 0
    if len(temp) == 1:
        return temp[0]
    product = 1
    if even:
        for i in range(0, len(temp)):
            product *= temp[i]
    else:
        endProduct = 1
        startProduct = 1
        saved1 = 0
        saved2 = len(temp) - 1
        noPositive = True
        i = 0
        while temp[i] > 0:
            noPositive = False
            startProduct *= temp[i]
            saved1 = i + 1
            i += 1
        startProduct *= temp[i]
        # print(startProduct)
        i = len(temp) - 1
        while temp[i] > 0:
            noPositive = False
            endProduct *= temp[i]
            saved2 = i - 1
            i -= 1
        endProduct *= temp[i]
        # print(endProduct)
        # print(noPositive)
        if noPositive:
            if temp[0] < temp[len(temp) - 1]:
                saved2 = len(temp) - 1
                saved1 = 0
            else:
                saved1 = 0
        # print(saved1)
        # print(saved2)
        if saved1 == saved2:
            if startProduct < endProduct:
                product = startProduct/temp[saved1]
                return int(product)
            else:
                product = endProduct / temp[saved1]
                return int(product)
        # print(saved1)
        for i in range(saved1 + 1, saved2):
            product *= temp[i]
        # print(product)
        if startProduct < endProduct:
            product *= startProduct
        else:
            product *= endProduct
    return product


class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        maxProduct = -10
        i = 0
        zero = False
        allZeros = True
        while i < len(nums):
            temp = []
            even = True
            while i < len(nums) and nums[i] != 0:
                allZeros = False
                temp.append(nums[i])
                if nums[i] < 0:
                    even = not even
                i += 1
            # print(temp)
            product = maxProductNoZeros(temp, even)
            if i != len(nums) and nums[i] == 0:
                zero = True
            if product > maxProduct:
                maxProduct = product
            i += 1
        if allZeros:
            return 0
        if zero and maxProduct < 0:
            maxProduct = 0
        return maxProduct


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(maxProductNoZeros([-3, -1, -1], False))
    print(obj.maxProduct([-2,0,-1]))
    print(obj.maxProduct([1,0,-1,2,3,-5,-2]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
