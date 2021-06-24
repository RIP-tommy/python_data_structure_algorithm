def plus(a, b):
    return int(a) + int(b)

def minus(a, b):
    return int(a) - int(b)

def multiply(a, b):
    return int(a) * int(b)

def cal(arr):
    res = int(arr[0])
    for idx in range(1, len(arr)):
        if (arr[idx] == '+'):
            res = plus(res, arr[idx + 1])
        elif (arr[idx] == '-'):
            res = minus(res, arr[idx + 1])
        elif (arr[idx] == '*'):
            res = multiply(res, arr[idx + 1])
    return res

def solution(expression):
    expression = expression.replace('-', ' - ')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('*', ' * ')
    expression = expression.split(' ')
    answer = cal(expression)
    return answer

temp = solution("100-200*300-500+20")
print(temp)