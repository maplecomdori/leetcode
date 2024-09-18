class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {order[i]: i for i in range(len(order))}

        # compare two words at a time
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i+1]

            # compare letter by letter
            # if letter from the second word comes first => return False
            i, j = 0, 0
            while i < len(first) and j < len(second):
                if order_map[first[i]] > order_map[second[j]]:
                    return False
                elif order_map[first[i]] < order_map[second[j]]:
                    break
                i += 1
                j += 1

            # if first word has more letters than second word
            # and first word has all the letters of the second word => false
            if j == len(second) and i < len(first):
                return False
        return True
