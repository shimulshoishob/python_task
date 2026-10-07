vowel = ['a', 'e', 'i', 'o', 'u']
for i in vowel:
    print(i)
#range not included upper bound
#if lower limit not given then start from 0
#range(lower bound, upper bound, increment)
for i in range(1, 10):
    print(i)
scour = [12, 2, 23, 67, 43, 13]
maximum = 0
for i in scour:
    if i > maximum:
        maximum = i
print(maximum)

#sum of 1 to 100
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
