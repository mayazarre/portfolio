import csv
import string



# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
print(elementsList[0])

# print the last element
print(elementsList[len(elementsList)-1])
# print all the elements
print(elementsList)


Country = input("What country would you like us to find?: ")

begin = 0
end = len(elementsList) - 1
index = int((end - begin)/2)

while elementsList[index] != Country:
    if Country < elementsList[index]:
        begin = begin
        end = index
        index = int((end - begin)/2) + begin
    elif Country > elementsList[index]:
        begin = index + 1
        end = end
        index = int((end - begin)/2) + begin
    else:
        print(index)

print(Country)
print("is the")
if index == 1:
    print(str(index)+"st")
elif index == 2:
    print(str(index)+"nd")
elif index == 3:
    print(str(index)+"rd")
elif index > 3:
    print(str(index)+"th")
print("country in the list")
print("Done!")
