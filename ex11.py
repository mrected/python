print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)

print 'Add this...',
add_this = raw_input('> ')
print '...to this',
to_this = raw_input('> ')
print int(add_this) + int(to_this)