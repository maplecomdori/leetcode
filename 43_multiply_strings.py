class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        mask1 = 1  # 10 ** n for num1

        for i in range(len(num1) - 1, -1, -1):
            first = int(num1[i])
            total = 0
            mask2 = 1  # 10 ** n for num2
            for j in range(len(num2) - 1, -1, -1):
                second = int(num2[j])
                total += first * second * mask2
                mask2 *= 10

            res += total * mask1
            mask1 *= 10

        return str(res)

        # array solution
        if num1 == "0" or num2 == "0":
            return "0"

        new1 = [int(c) for c in num1[::-1]]
        new2 = [int(c) for c in num2[::-1]]
        result = [0] * (len(new1) + len(new2))

        # Multiply store the result
        for i in range(len(new1)):
            for j in range(len(new2)):
                result[i + j] += new1[i] * new2[j]

        # Handle carry
        for i in range(len(result)):
            if result[i] >= 10:
                result[i + 1] += result[i] // 10
                result[i] %= 10

        # Remove leading zeros (if any)
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert to string and reverse back
        return ''.join(str(d) for d in reversed(result))