#define a function called cheese and crackers, passing in information abount cheese count and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#print the amount of cheese
	print "You have %d cheeses!" % cheese_count
	#print the number of boxes of crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#passing in numbers to the function	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#passing in variable references
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#passing in math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#passing in both
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def n_problems(problems):
	print "I've got %d problems but a bitch ain't one" % problems
	
n_problems(99)

n_problems(10 * 10 - 1)

problems = 99
n_problems(problems)

problems = int(raw_input("How many problems do I have? "))
n_problems(problems)

problems = 90
n_problems(problems + 9)

