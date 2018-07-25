

x = "There are %d types of people." % 10   #inputing character into string
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)  # Inputting characters into string
print x
print y
print "I said: %r." % x # inputting x characters into %r
print "I also said: '%s'." %y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w + e

#key notes "string" % character.   command inputs the character into the string
#key the %_ is the replaced value in the string 

# output
#There are 10 types of people.
#Those who know binary and those who don't.
#I said: 'There are 10 types of people.'.
#I also said: 'Those who know binary and those who don't.'.
#Isn't that joke so funny?! False
#This is the left side of...a string with a right side.
