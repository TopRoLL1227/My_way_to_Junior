# from collections import Counter
    
# def count_occurrences(input_str):
#     words = input_str.lower().split()
#     return Counter(words)


# print(count_occurrences("The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."))


def repeat(input):
    words_str = input.lower().split()
    new_words = {}
    
    for words in words_str:
        if words in new_words:
            new_words[words] += 1
        else:
            new_words[words] = 1
    
    return new_words
    

print(repeat("The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."))


