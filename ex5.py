name = 'Zed A. Shaw'
age = 35
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually he's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky...
print "If I add %d, %f and %d I get %d." % (
    age, height, weight, age + height + weight)
    
print "Anywhere else in the world, he would weigh %r kilos and be %r cm tall." % (
    round(weight * 0.453592,1), round(height * 2.54,1))
