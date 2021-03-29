string_list=[]
n=int(input("Enter number of strings to be added: "))

for i in range(0,n):
    s=input("String > ")
    string_list.append(s)


for i in range(0,n):
    for j in range (0,n-1-i):
        if len(string_list[j])>len(string_list[j+1]):
            large=string_list[j]
            string_list[j]=string_list[j+1]
            string_list[j+1]=large

print(string_list)