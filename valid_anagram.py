def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = "anagram"
word2 = "nagaram"

print(are_anagrams(word1, word2))