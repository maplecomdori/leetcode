from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.i_to_n = {}  # {index: number}
        self.n_to_i = {}  # {number: [index]}

    def change(self, index: int, number: int) -> None:
        # print('change', index, number)

        if index in self.i_to_n:
            # index is already in use => clean up old record
            old_number = self.i_to_n[index]
            ss = self.n_to_i[old_number]
            ss.discard(index)

        if number not in self.n_to_i:
            # haven't seen this number
            ss = SortedSet()
            ss.add(index)
            self.n_to_i[number] = ss
            self.i_to_n[index] = number
        else:
            # seen this number
            self.n_to_i[number].add(index)
            self.i_to_n[index] = number

    def find(self, number: int) -> int:
        if number not in self.n_to_i or not self.n_to_i[number]:
            return -1

        return self.n_to_i[number][0]


"""
find(10) => -1
2:10    { 10: [2] }
1:10    { 10: [1, 2] }
3:10    { 10: [1, 2, 3] }
5:10    { 10: [1, 2, 3, 5] }
find(10) => 1
change(1,20), 1:20 { 10: [2,3,5], 20: [1] }
find(10) => 2


"""