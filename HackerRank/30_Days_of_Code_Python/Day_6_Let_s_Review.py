# Solution 1 : for HackerRank 
STDIN = input("")
for N in range(int(STDIN)):
    S = input()
    print(S[::2], S[1::2])

# Solution 2 : better result in Terminal
STDIN = input("Enter a word: ")
word1 = ""
word2 = ""

for index1 in range(len(STDIN)):
    if index1 % 2 == 0:
        word1 = str(word1) + STDIN[index1]
for index2 in range(len(STDIN)):
    if index2 % 2 != 0:
        word2 = str(word2) + STDIN[index2]

print(word1, word2)
