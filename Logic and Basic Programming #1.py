a = int(input('첫번째 정수 입력: '))
b = int(input('두번째 정수 입력:'))
c = int(input('세번째 졍수 입력:'))
d = int(input('네번째 정수 입력:'))
e = int(input('다섯번째 정수 입력: '))

A = [a, b, c, d, e]

for i in range(len(A)):
    k = len(A)-i
    for j in range(1, k):
      if A[j-1] >= A[j]:
        r = A[j-1]
        A[j-1] = A[j]
        A[j] = r
        
print(A[3])
