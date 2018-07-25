formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
      "I had this thing.",
      "That you could type up right.",
      "But it didn't sing.",
      "so I said goodnight."
)

#formatter = "%r %r %r %r"
#most important below
#!going to be replacing all words title formatter with "r r r"
#but the r's represent and will be replaced with what comes after the %
# I also believe the comas puts things on the same line


#formatter with whatever the specified formatter is!
#-- The first formater = r% then (r% = 1)
#print formatter % (1, 2, 3, 4)
#print formatter % ("one", "two", "three", "four")
#print formatter % (True, False, False, True)
#print formatter % (formatter, formatter, formatter, formatter)
#print formatter % (
#      "I had this thing.",
#      "That you could type up right.",
#      "But it didn't sing.",
#      "so I said goodnight."
#)

#Output below

#


#1 2 3 4
#'one' 'two' 'three' 'four'
#True False False True
#'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
#'I had this thing.' 'That you could type up right.' "But it didn't sing." 'so I said goodnight.'
