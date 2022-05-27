# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from collections import Counter

def find_anagrams(st1, st2):

	if(Counter(st1) == Counter(st2)):
		print("True")
	else:
		print("False")

st1 = "hello"
st2 = "check"
find_anagrams(st1, st2)

def find_anagrams(st3, st4):

	if(Counter(st3) == Counter(st4)):
		print("True")
	else:
		print("False")

st3 = "below"
st4 = "elbow"
find_anagrams(st3, st4)
