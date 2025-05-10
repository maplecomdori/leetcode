class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def is_valid(first, second):
            if not (second <= 0.5 * first + 7) and not (second > first) and not (second > 100 and first < 100):
                return True
            return False

        counter = {}
        for age in ages:
            counter[age] = counter.get(age, 0) + 1

        res = 0
        for first_age, first_freq in counter.items():
            for second_age, second_freq in counter.items():
                if not is_valid(first_age, second_age):
                    continue
                if first_age == second_age:
                    # don't send a request to self
                    res += first_freq * (second_freq - 1)
                else:
                    res += first_freq * second_freq

        return res

        # brute force
        # start from the oldest person, compare with younger people
        count = 0

        for i in range(len(ages) - 1):
            first = ages[i]
            for j in range(i + 1, len(ages)):
                second = ages[j]
                # first sends letter to second
                if not (second <= 0.5 * first + 7) and not (second > first) and not (second > 100 and first < 100):
                    count += 1
                # second sends letter to first
                if not (first <= 0.5 * second + 7) and not (first > second) and not (first > 100 and second < 100):
                    count += 1
        return count


"""
y > 0.5x + 7            not to a person about half his age + 7 => more than half of my age
y > x                   not to an older person  => older than me
y > 100 and x < 100     not between 2 digits and 3 digits


20  30  30  100 100 100 110
20:1
30:2
100:3
110:1

20 => 0
30 => 2 * 1 = 2
100 => 3 * 2 = 6
110 => 3 = 3

= 11

"""