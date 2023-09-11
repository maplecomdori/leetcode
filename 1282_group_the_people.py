class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}  # {size: [index]}

        for i, gs in enumerate(groupSizes):
            if gs in dic:
                dic[gs].append(i)
            else:
                dic[gs] = [i]

        res = []
        for gs, idx_lst in dic.items():
            lst = []
            for i in range(len(idx_lst)):
                lst.append(idx_lst[i])
                if len(lst) == gs:
                    res.append(lst)
                    lst = []
        return res
