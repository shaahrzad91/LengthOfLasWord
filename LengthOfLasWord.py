s= "Hello World"
words = s.split(' ')
word =[ w for w in words if w != '']
if (len(word) == 0):
    answer = 0
else:
    word= word[-1]
    answer = len(word)
        
print(answer)   