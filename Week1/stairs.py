# Нарисовать лесенку из решеток

k = int(input())
for i in range(k):
    print(" "*(k-i-1)+"#"*(i+1))