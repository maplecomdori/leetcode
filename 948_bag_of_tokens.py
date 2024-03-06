class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # maximize total score
        # score = 0
        # face up if power >= tokens[i], power -= tokens[i], score += 1
        # face down if score > 0, power += tokens[i], score -= 1
        if not tokens:
            return 0
        score = 0
        tokens.sort()
        left = 0
        right = len(tokens) - 1

        while left < right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                return score
        if power >= tokens[left]:
            score += 1
        return score

