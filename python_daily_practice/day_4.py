Q1: 
nums = [1, 2, 3, 4]
print(nums[4])
User Answer: index eroor
Verdict: Sahi

Q2: 
a = 10
b = 20
print(a > b and b > a)
User Answer: False
Verdict: Sahi

Q3: 
for i in range(3):
    print(i)
User Answer: 0
1
2
Verdict: Sahi

Q4: 
def add(x, y=5, z):
    return x + y + z
User Answer: eroor ayegi
Verdict: Sahi

Q5: 
x = [1, 2, 3]
y = x
y.append(4)
print(x)
User Answer: [1,2,3,4]
Verdict: Sahi

Q6: 
x = 5
y = "5"
print(x + y)
User Answer: error
Verdict: Sahi

Q7: 
for i in range(1, 5, 0):
    print(i)
User Answer: 1
Verdict: Sahi

Q8: 
def test(a, b=[]):
    b.append(a)
    return b

print(test(1))
print(test(2))
User Answer: [1]
[1,2]
Verdict: Sahi

Q9: 
print(bool("False"))
User Answer: True
Verdict: Sahi

Q10: 
try:
    print(1/0)
except:
    print("error")
finally:
    print("done")
User Answer: error
finally
Verdict: Sahi

Q11: 
print("Hello" * 3.0)
User Answer: error
Verdict: Sahi

Q12: 
a = [1, 2, 3]
print(a[::0])
User Answer: []
Verdict: Sahi

Q13: 
print(0.1 + 0.2 == 0.3)
User Answer: False
Verdict: Sahi

Q14: 
x = (1, 2, 3)
x[0] = 5
User Answer: error 
copz tuple immutab;e
Verdict: Sahi

Q15: 
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)
User Answer: 1 0
2 0
2 1
Verdict: Sahi