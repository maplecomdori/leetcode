class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            # compare which concatenation order results in a greater number
            if x + y > y + x:
                return 1
            else:
                return -1

        nums = [str(n) for n in nums]
        nums.sort(reverse=True, key=cmp_to_key(compare))

        return str(int("".join(nums)))


"""
10  2
210

3   30  34  5   9
9   5   34  3   30


same number of digit => compare
different number of digit => 
33 3 => doesn't matter which one comes first
34 3 => 343 > 334

"""