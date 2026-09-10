candy = [2,3,5,1,3]
extra_candy = 3
greatest = max(candy)
result = []
for i in range(len(candy)):
    if candy[i] + extra_candy >= greatest:
        result.append(True)
    else:
        result.append(False)
print(result)