age = 24
days = 11
print("My age is " + str(age) + " years")
print("My age is {0} years and {1}".format(age,days))

print ("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
       .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print ("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, Dec".format(31))
print ("jan {2}, Feb:{0}, Mar: {1}".format(28,30,31))
print("""
Jan: {2}
Feb: {0}
Mar: {1}
""".format(28,30,31))