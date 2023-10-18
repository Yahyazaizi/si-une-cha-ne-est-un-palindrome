chaine=input("svp done une chain:")
l1=list(chaine)
p=l1.copy()
l1.reverse()
print(l1)
print(p)
if p==l1:
    print("si une chaîne est un palindrome.",chaine)
else:
    print("si une chaîne est non palindrome.",chaine)
