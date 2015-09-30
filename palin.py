import sys

def palin(word):
    result = "TRUE"
    l = len(word)-2
    for i in range (0,len(word)/2):
        if (word[i] != word[l-i]):
   #         print(word[i])
   #         print("lala")
   #         print(word[len(word)-1-i])
            result = "FALSE"
   #         break
    print(result)

word = sys.stdin.readline()
palin(word)


