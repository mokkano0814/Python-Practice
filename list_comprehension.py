'''double = []
my_list = [1, 2, 3]
for item in my_list:
    double.append(item * 2)
print(double)

users = [{'name' : 'Manuel', 'age': 31}, {'name' : 'Max', 'age': 30}, {'name' : 'Dirk', 'age': 38}]
for user in users:
    print(user)'''
'''
list_1 = ["Mate", "Szau", "Dani"]
print(list_1[0])
print(len(list_1 ))

list_2 = [["Rolf", 24],
          ["Bob", 30],
          ["Anne", 27]]
print(list_2[1][1])

list_2.append("Mateka")
print(list_2)

#tuples:

short_tuple = ("Rolf", "Bob")
print(short_tuple)
'''
#sets:
'''
art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie", "Anne"}
art_friends.add("Jen")
print(art_friends)
art_friends.remove("Jen")
print(art_friends)

art_and_science = art_friends.intersection(science_friends) # közös elemek
print(art_and_science)

all_friends = art_friends.union(science_friends) #kiírni az összeset
print(all_friends)

art_but_not_sciences = art_friends.difference(science_friends) # meg tudjuk őket különböztetni
print(art_but_not_sciences)

set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)
'''
#dictionaries
'''
friends = [("Rolf", 24), ("Adam" , 30),("Anne", 27)]
friends_ages = dict(friends)
print(friends_ages)
'''
'''
grades = [80,75,90,100]
sum_grades = sum(grades)
print(sum_grades)

len_grades = len(grades)
print(len_grades)

average = sum_grades / len_grades
print(average)
'''
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")
print("molnárúr")