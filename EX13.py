#create a script that convertsall items of the range to strings
my_range = range(1, 21)
#expected output ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
print(list(map(str, my_range)))