def solution(num):
    sum = 0
    for i in range(3,num):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
