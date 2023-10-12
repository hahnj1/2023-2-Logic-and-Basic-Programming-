a = int(input('숫자를 입력하세요: '))
b = int(input('숫자를 입력하세요: '))

def MAX_F(a,b):
    if a >= b:
     M = a
    else:
     M = b
    return M

print(MAX_F(a,b))

M = MAX_F(a,b)

if M >= 1 and M <= 10:
 print('*'*M)
else:
 print('1 이상 10 이하의 숫자를 입력하세요.')
