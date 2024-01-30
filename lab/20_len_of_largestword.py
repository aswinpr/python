wordlist=[]
n=int(input("enter the number of words : "))
for i in range(n):
    words=input("enter the words:")
    wordlist.append(words)

max_length=len(wordlist[0])
longest_word=wordlist[0]

for i in wordlist:
    if len(i)>max_length:
        max_length=len(i)
        longest_word=i
print("longest word is",longest_word)
print("length of longest word is",len(longest_word))
