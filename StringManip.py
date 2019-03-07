#In the language of your choice, write a method that modifies a string using the following rules:
#1. Each word in the input string is replaced with the following: the first letter of the word, the count of distinct letters between the first and last letter, 
# and the last letter of the word. For example, “Automotive parts" would be replaced by "A6e p3s".
#2. A "word" is defined as a sequence of alphabetic characters, delimited by any non-alphabetic characters.
#3. Any non-alphabetic character in the input string should appear in the output string in its original relative location.



#Write your code below.

#Assumptions: If a one letter word, print first character, then 0.
#             If a two letter word, print first character, then 0, then last character.
#             If a non-alpha character is in the middle of a word, it should be there in the output, no spaces separating it from the letters around it.

#Test cases
#1. Automotive parts                    = A6e p3s
#2. Gatorade                            = G5e
#3. A motive gear                       = A0 m4e g2r
#4. Race car!                           = r2e c1r!
#5. Franklin, Esq.                      = F6n, E1q.
#6. An iguana                           = A0n i4a
#7. Extr3mely d!fficu1t te$t            = E2r3m2y d0!f3u1t0 t0e$t0

def strMod():
    print("Input a string")
    st = input()
    temp = ''
    newtemp = []

    for i in range(len(st)):
        if st[i].isalpha() != True:
            if temp != '':
                newtemp.append(temp)
                temp = ''
            newtemp.append(st[i])
        else:
            temp += st[i]
    newtemp.append(temp)
    temp = ''

    for j, newSt in enumerate(newtemp):
        if newSt.isalpha():
            if len(newSt) < 2:
                temp = newSt[0] + str(0)
                newtemp[j] = temp
                temp = ''
            else:
                temp = newSt[0] + str(len(set(newSt[1:-1]))) + newSt[-1]
                newtemp[j] = temp
                temp = ''

    print(''.join(newtemp))

strMod()