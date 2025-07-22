# import redis


# r = redis.Redis(host='localhost', port=6379, db=0)

# # r.set("key1", 23, ex=15)

# print(r.get("key1"))
# print(r.get("key1").decode())



# # 
# x = {"key1": 23}
# x['key2'] = 34

def rev(lst):
    l = ""
    for i in range(len(lst)-1, -1, -1):
        l += lst[i]
    return l


sentence = "I love Python"
word=[]
result=[]
for i in list(sentence) + [" "]:
    if i !=" ":
        word.append(i)
    elif i==" ":
        result.append(rev(word))
        word = []

print(word)
print(result)

st = ""
for i in result:
    st += " " + i

print(result)

#######################
word = ""
result = ""

for i in sentence:# i =char
    if i != " ":
        word =i+word   
    else:
        result += word + " "
        word = ""

result += word 
print(result)

