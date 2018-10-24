# var=['a','b','c','f','g','k','l','m','n','k']
# var=sorted(var)
# print(''.join(var))

# def value_string(sention):
#     lower=0
#     upper=0
#     for i in sention:
#         if i.islower():
#             lower+=1
#         if i.isupper():
#             upper+=1
#     print("The Lower Values: ",lower)
#     print("The Upper valuse: ",upper)
# var=input("enter the name: ")
# value_string(var)

# def replace(sent,words):
#     return sent.replace(words,"*" * len(words))
# sent=input("enter the sent: ")
# words=input("enter the words: ")
# print(replace(sent,words))

def replace_char(sent,words):
    for i in sent:
        if i in words:

sent=input("enter the sent: ")
words=input("enter the words: ")
print(replace_char(sent,words))