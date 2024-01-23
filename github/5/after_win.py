import re

def remove_characters(text):
    return re.sub(r'[،:؛.؟!٬٫]+', '', text)

def similar_words(n, sentence, target_word):
    sentence = remove_characters(sentence)
    words = sentence.split()

    result = [word for word in words if distance(word, target_word) <= n]

    return result

def distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    max_len = max(len1, len2)
    word1 += '_' * (max_len - len1)
    word2 += '_' * (max_len - len2)

    distancew = sum(c1 != c2 for c1, c2 in zip(word1, word2))

    return distancew


n = int(input())
sentence = input()
target_word = input()

result = similar_words(n, sentence, target_word)
for word in result:
    print(word)
