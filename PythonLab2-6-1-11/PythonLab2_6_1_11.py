#Original
#hour = int(input("Starting time (hours): "))
#mins = int(input("Starting time (minutes): "))
#dura = int(input("Event duration (minutes): "))
# Write your code here.

#Scenario
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#Get total minutes
a = mins + dura
#Get hours in relation to minutes
b = hour + (a // 60)

#Get event time hours
et_hrs = b % 24
#Get end time minutes
et_min = a % 60

#Display event time hours and minutes; sep removes " " (the spaces)
print("\nEvent time is: ", et_hrs, ":", et_min, sep="", end="\n\n")
