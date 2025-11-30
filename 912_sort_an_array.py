class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(a_lst, b_lst):
            a_idx = 0
            b_idx = 0
            res = []
            while a_idx < len(a_lst) or b_idx < len(b_lst):
                if a_idx < len(a_lst) and b_idx < len(b_lst):
                    a = a_lst[a_idx]
                    b = b_lst[b_idx]
                    if a < b:
                        res.append(a)
                        a_idx += 1
                    else:
                        res.append(b)
                        b_idx += 1
                elif a_idx < len(a_lst):
                    res.append(a_lst[a_idx])
                    a_idx += 1
                else:
                    res.append(b_lst[b_idx])
                    b_idx += 1
            return res

        def merge_sort(lst):
            if len(lst) == 1:
                return lst

            mid = len(lst) // 2
            left = merge_sort(lst[:mid])
            right = merge_sort(lst[mid:])

            sorted_lst = merge(left, right)
            return sorted_lst

        return merge_sort(nums)


'''
5   2   3   1

5 2     3 1

5,2     3,1

2 5     1 3
1 2 3 5

'''