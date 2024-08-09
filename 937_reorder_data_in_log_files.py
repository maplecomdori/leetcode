class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        lst_let = []
        lst_dig = []

        for log_str in logs:
            lst_str = log_str.split()

            if lst_str[-1].isdigit():
                lst_dig.append(log_str)
            else:
                new_lst_str = [lst_str[0], " ".join(lst_str[1:])]
                lst_let.append(new_lst_str)

        lst_let.sort(key=lambda x: (x[1], x[0]))
        for i in range(len(lst_let)):
            lst_let[i] = " ".join(lst_let[i])
        return lst_let + lst_dig