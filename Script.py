print("BounDos\n")
import random
def wordpad():
	print("You choosen wordpad")
	inp2=input("What you want to do sir\nEnter:\ns for working with sample file\nf for working with new file\n")
	if inp2=="s":
		print("You chosen sample file\nSAMPLE FILE:\n")
		sf=input()
		print("YOUR SAMPLE FILE:\n",sf)
	elif inp2=="f":
		ch1=input("What you want to do sir\nEnter:\np for creating and working with new file\ni for working with the past file\n")
		if ch1=="p":
			print("You want to work and create a new file")
			tcf=input("Enter your file name with extension:")
			text=input("YOUR FILE:\n")
			a=open(tcf,"x")
			b=open(tcf,"w")
			b.write(text)
		elif ch1=="i":
			print("You want to work with a past file")
			tcf2=input("Enter:\nor to read the file\nm for edit the file\n")
			if tcf2=="or":
				inps1=input("Enter your file name with extension:")
				try:
					n1=open(inps1,"r")
					c=n1.read()
					print(c)
				except Exception as error:
					error=f"There is no file named {inps1}"
					print(error)
			elif tcf2=="m":
				inps2=input("Enter your file name with extension:")
				try:
					text2=input("FILE:\n")
					n2=open(inps2,"a")
					n2.write(text2)
				except Exception as error2:
					error2=f"There is no file named {inps2}"
					print(error2)
inp1=input("What you want to do sir :)\nEnter h for help\n")
if inp1=='h':
	print("w for open wordpad\ng for playing game")
elif inp1=="w":
	wordpad()
elif inp1=="g":
	ch=["rock","paper","scissor"]
	user=input()
	comp=random.choice(ch)
	print(f"YOUR CHOICE:{user}\nCOMPUTERS CHOICE:{comp}")
	if user in ch:
		if user==comp:
			print("TIDE")
		elif user=="rock" and comp=="paper":
			print("COMPUTER WIN!!")
		elif user=="paper" and comp=="rock":
			print("YOU WIN!!")
		elif user=="paper" and comp=="scissor":
			print("COMPUTER WIN!!")
		elif user=="scissor" and comp=="paper":
			print("YOU WIN!!")
		elif user=="scissor" and comp=="rock":
			print("COMPUTER WIN!!")
		elif user=="rock" and comp=="scissor":
			print("YOU WIN!!")
		else:
			print("YOUR CHOICE IS UNDEFINED")
	else:
		print("Your choice is undefined :(\nEnter again:\n")
