## 함수 선언부
def add_func(n1, n2) :
    res = n1 + n2
    return res

def sub_func(n1, n2) :
    res =  n1 - n2
    return res

def dou_func(n1, n2) :
    res = n1 * n2
    return res

def div_func(n1, n2) :
    res =  n1 / n2
    return res

## 전역 변수부
a, b, res = 14, 27, 0

## 메인 코드부
res = add_func(a, b)
print(a, ' + ', b, ' = ', res)

res2 = sub_func(a,b)
print(a, ' - ', b, ' = ', res2)

res3 = dou_func(a, b)
print(a, ' * ', b, ' = ', res3)

res4 = div_func(a, b)
print(a, ' / ', b, ' = ', res4)


add apink;
