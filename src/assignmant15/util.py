
def count_word_occurrences(words):
    word_index = {}       # store first appearance index
    occurrences = []      # counts aligned with order of appearance
    order = []            # order of distinct words

    for word in words:
        if word in word_index:
            idx = word_index[word]
            occurrences[idx] += 1
        else:
            word_index[word] = len(order)
            order.append(word)
            occurrences.append(1)

    return len(order), occurrences