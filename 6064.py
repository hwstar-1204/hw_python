#3개수중에 제일 작은 수 삼항연산으로 구하기
#a if(a<b) else b -> 조건에 만족하면 a 아니면 b 라는 구문
#구문이 복잡해보이지만 똑같은 구문이 2개가 섞여있다. 
# 제일 큰 수를 구할려면 부등호 기호만 반대로 바꾸면 된다. 

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if(a<b) else b) if((a if(a<b) else b) < c) else c
print(int(d))