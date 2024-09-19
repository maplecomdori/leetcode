class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        lst = sentence.split()
        vowel = set(['a', 'e', 'o', 'i', 'u', 'A', 'E', 'I', 'O', 'U'])
        # for each word
        for idx, word in enumerate(lst):

            # check first letter => vowel or consonant
            if word[0] in vowel:
                word = word + 'ma'
            else:
                word = word[1:] + word[0] + 'ma'

            # add 'a' * (index - 1) at the end
            word += 'a' * (idx + 1)
            lst[idx] = word

        return " ".join(lst)


'''
begins with vowel => append 'ma' at the end of the word
begins with conso => remove first letter and append at the end, then add 'ma'
append a X (index + 1) at the end

'''