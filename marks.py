marks=[[78,76,94,86,88],[91,71,98,65],[95,45,78]]
i=0
year=1
while i<len(marks):
    a=0
    sum=0
    while a<len(marks[i]):
        k=marks[i][a]
        sum=sum+k
        a=a+1
    avg=sum//len(marks[i])
    print("avg of",year,"year=",avg)
    i=i+1
    year=year+1