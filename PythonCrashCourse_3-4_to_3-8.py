#3-4
dinner_invites = ["Mom", "Dad", "Grandma"]
for i in range(3):
    print("Dear " + dinner_invites[i] + ", please come to my dinner party.")

#3-5    
print("Unfortunately, Grandma cannot make it to the dinner party.")
dinner_invites[2] = "Grandpa"
for i in range(3):
    print("Dear " + dinner_invites[i] + ", please come to my dinner party.")
    
#3-6    
print("I've found a bigger dinner table so I'm going to invite more people.")
dinner_invites.insert(0, "Brother")
dinner_invites.insert(2, "Sister")
dinner_invites.append("Friend")
for i in range(6):
    print("Dear " + dinner_invites[i] + ", please come to my dinner party.")

#3-7
print("Unfortunately the dinner table will not arrive on time so I only have space for 2 guests.")
revoked_dinner_invites = dinner_invites.pop(2)
print("Sorry " + revoked_dinner_invites + ", I cannot invite you to dinner.")
revoked_dinner_invites = dinner_invites.pop(2)
print("Sorry " + revoked_dinner_invites + ", I cannot invite you to dinner.")
revoked_dinner_invites = dinner_invites.pop(2)
print("Sorry " + revoked_dinner_invites + ", I cannot invite you to dinner.")
revoked_dinner_invites = dinner_invites.pop(2)
print("Sorry " + revoked_dinner_invites + ", I cannot invite you to dinner.")
for i in range(2):
    print("Dear " + dinner_invites[i] + ", you are still invited to my dinner party.")
del dinner_invites[0]
del dinner_invites[0]
print(dinner_invites)

#3-8
places = ["Campania", "New Orleans", "Munich", "Seoul", "Tokyo"]
print(places)
print(sorted(places))
print(sorted(places, reverse=True))
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

class1 = 32
class2 = 45
class3 = 51
class1_groups = class1 // 5
class2_groups = class2 // 7
class3_groups = class3 // 6
class1_leftover = class1 % 5
class2_leftover = class2 % 7
class3_leftover = class3 % 6
print("Number of students in each group:")
print("Class 1: " + str(class1_groups))
print("Class 2: "+ str(class2_groups))
print("Class 3: "+ str(class3_groups))
print("Number of students leftover:")
print("Class 1: " + str(class1_leftover))
print("Class 2: " + str(class2_leftover))
print("Class 3: " + str(class3_leftover))

pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter / 2
circumference = 2 * pi * pie_radius
circumference_msg = "Jimmy’s pie has a circumference: "
print(circumference_msg, circumference)

velocity = 343
frequency = 256
wavelength = velocity/frequency
print("The speed (m/s): " + str(velocity))
print("The frequency (Hz): " + str(frequency))
print("The wavelength (m): " + str(wavelength))




