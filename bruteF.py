<<<<<<< HEAD
''' the needed libraries for this code to be able to open files 
from a remote URL and hash password guesses into SHA-1. To 
include them, create a new Python3 file in your IDE and type the 
following into the first line'''

from timeit import default_timer as timer
from urllib.request import urlopen, hashlib

'''//this is where I want to make a read from local file work
but still giving me trouble

get hash from user**this is normally where you pull from url**
print("enter password to crack: ")
sha1hash = input()
print(sha1hash)

open a file full of passwords
f = open ("test.txt", "r")
print(f.read())

#LIST_OF_COMMON_PASSWORDS = str(f)
'''
#start timer to measure execution time for program
start = timer()

=======
''' 
urllib : http related libary
urllib.urlopen : open file from url
hashlib : hash algorithms to use in code
'''
from urllib.request import urlopen, hashlib

#get hash from user to crack
>>>>>>> 47c1cdeeab4e2995534823648056bce44806178c
sha1hash=input("Enter input the hash to crack : ")

#hash the users input
sha1hash = hashlib.sha1(bytes(sha1hash, 'utf-8')).hexdigest()
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')


#guess from list
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
	print("this is whats in guess", guess)

	#hash the guessed password
	hashedGuess = hashlib.sha1(bytes(guess,'utf-8')).hexdigest()
	print("this is whats in hashedGuess", hashedGuess)

	#compare the hash user gave to guess
	if hashedGuess == sha1hash:

		#if match print ..
		#if doest, loop back
		print("The password is ", str(guess))
		
		#end the exec timer
		end = timer()
		print(end - start) #time in seconds
		quit()
	elif hashedGuess != sha1hash:
		print("Password guess ", str(guess), " does not match, ..trying next..")

#let user know we are at end of file
print("Password not in database, we'll get them next time.")

#end the exec timer
end = timer()
print(end - start) #time in seconds
