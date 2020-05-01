import math 

num = 38
result = 0
fresl = 0
while num > 0:
    digit = num % 10
    result = result + digit  # 0 + 8
    num = num // 10   # 8 removed

while result > 0:
    digit_ = result % 10
    fresl = fresl + digit_
    result = result // 10

print(fresl)
