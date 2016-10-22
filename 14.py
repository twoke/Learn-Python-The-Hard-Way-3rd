from sys import argv

script, user_name, city = argv
prompt = 'Please type the answer:'

print  "Hi, %s from %s,I'm the %s script." % (user_name, city, script)
print "I'd like to ask you a few questions."
print "Do you like me  %s?" % user_name
likes = raw_input(prompt)

print "what's the weather like today in %s?" % city
weather = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
The weather in your city is %s.
But I can't feel it because I'm a robot.
And you have a %r computer.Nice.
""" % (likes, weather, computer)
