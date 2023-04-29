import random

rand = 1

while rand != 0:

	rand = random.randint(0,100)

	if rand % 2 != 0:
		print(rand * 3)
	else:
		print(rand * 2)

print("\nrand = ", rand, "\n")