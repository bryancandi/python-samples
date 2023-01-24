name = input("\nWhat is your name?\n")
print("Hello, " + (name) + "!\n")

color = input("What is your favorite color?\n")
print((name) + "'s favorite color is " + (color) + ".\n")

mycolor = "red"
mycolorguess = input("Can you guess my favorite color?\n").lower()
while mycolorguess != mycolor:
	if mycolorguess == "stop":
		break
	print("That is not correct!")
	mycolorguess = input("Try again? Or type 'stop' to give up.\n").lower()
else:
	print("That is correct! " + (mycolor).title() + " is my favorite color!")

print("\nEnd.")
