#Create a algorithm tu find lowest value in a list
x = [3,5,7,10,8,20]
x.append(30)
largest = x[0]
for num in x:
    if num > largest:
       largest = num
print(largest)

# task: sum of all numbers nikalo bina sum() function use kiye
x = [4, 2, 9, 1, 7]
sum = 0 
for i in x:
    sum += +i
print(sum)
#task: count karo kitne numbers 5 se bade hain
x = [3, 6, 2, 8, 5]
num = 0
for i in x:
    if i > 5:
        num += 1
print(num)
# task: sabse chota number dhoondo (bina min() use kiye)
x = [12, 45, 3, 67, 21]
smallest = x[0]
for i in x:
    if i < smallest:
        smallest = i
print(smallest)
#Accumulation task: sab numbers ka average nikaalo
x = [2, 4, 6, 8, 10]
Average = 0
for i in x:
    Average += i/len(x)
print(Average)
## task: sirf even numbers ka sum nikaalo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 0
for i in x:
    if i % 2 == 0:
        num += i
print(num)
## task: list ko reverse order mein print karo (bina reverse() function use kiye)
x = [10, 20, 30, 40, 50]
for i in range(4,-1,-1):
    print(x[i])

    


