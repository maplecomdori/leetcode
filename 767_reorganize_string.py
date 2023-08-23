class Solution:
    def reorganizeString(self, s: str) -> str:

        # count chars and put it in max heap
        counter = Counter(s)
        h = [(-n, c) for c, n in counter.items()]
        heapq.heapify(h)

        builder = []
        while len(h) >= 2:
            # pop two most frequent characters at a time
            first_count, first_char = heapq.heappop(h)
            second_count, second_char = heapq.heappop(h)
            builder.append(first_char)
            builder.append(second_char)

            # decrement counts and add back to the heap if there are some left
            first_count += 1
            second_count += 1
            if first_count < 0:
                heapq.heappush(h, (first_count, first_char))
            if second_count < 0:
                heapq.heappush(h, (second_count, second_char))

        if h and h[0][0] < -1:
            # more than 2 of the same char remaining => not possible
            return ""
        if h and h[0][0] == -1:
            # only one letter left, add
            builder.append(h[0][1])

        return "".join(builder)
