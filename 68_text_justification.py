class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        builder = deque()
        output = []

        # for each word
            # check if the length of builder exceeds after adding this word
                # if so,
                # if one word in builder to the output=> left-justified
                # elif multiple words perform justification to the current builder and add the string to the output
                # reset builder with the current word
            # else add the word
        # handle last line

        for word in words:
            all_chars = sum([len(w) for w in builder])
            builder_length = all_chars + len(builder) + len(word)  # all chars, space req, curr len
            if builder_length > maxWidth:
                if len(builder) == 1:
                    only_string = builder[0]
                    len_empty = maxWidth - len(only_string)
                    builder.append(" " * len_empty)
                    output.append("".join(builder))
                else:
                    space_left = maxWidth - all_chars
                    num_need_extra_space = space_left % (len(builder) - 1)

                    even_space_length = space_left // (len(builder) - 1)
                    tmp = []

                    for i in range(num_need_extra_space):
                        tmp.append(builder.popleft())
                        tmp.append(' ' * (even_space_length + 1))

                    while builder:
                        tmp.append(builder.popleft())
                        tmp.append(' ' * even_space_length)

                    tmp.pop()  # remove last extra space
                    output.append("".join(tmp))

                builder = deque([word])
            else:
                builder.append(word)

        # handle last line (left-justified, no extra space between words)
        last_string = " ".join(builder)
        len_right_pad = maxWidth - len(last_string)
        output.append(last_string + (' ' * len_right_pad))

        return output


"""
len(each line) == maxWidth & left&right justified
pad with space, left first if even distribution is not possible
greedy

["This", "is", "an", "example", "of", "text", "justification."]
This    is    an
example  of text => more space on the left
justification

this is an example > 16

this is an => 8 characters, 8 empty space, 2 break => 6 each
example of text == 15 =>  13 char, 5 empty space, 2 break => 3 + 2 = 5 
justification == 13


DISTRIBUTION
3 break, 11 space => 4 4 3 (number of bigger space == 11 % 3 = 2)
3 break, 10 space => 4 3 3

LAST LINE (left-justified, no extra space between words)

ONE WORD => (left-justified)
"""