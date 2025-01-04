class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0  # count the number of flowers planted

        while i < len(flowerbed):
            prev_empty = True
            next_empty = True

            if flowerbed[i] == 0:
                if i > 0 and flowerbed[i - 1] == 1:
                    prev_empty = False

                if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                    next_empty = False

                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count == n:
                        return True

            i += 1

        return n <= count