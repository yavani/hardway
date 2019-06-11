def break_words(stuff):
	""" this function will break up word for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	""" sort the words ."""
	return sorted(words)

def print_first_word(words):
	""" print the first word after poping it off."""
	word = words.pop(0)
	print(word)

def print_last_word(words):
	""" print last word after poping it off."""
	word = words.pop(-1)
	print(word)
	

def sort_sentence(sentence):
	""" takes in a full sentence and return the sorted word ."""
	words= break_words(sentence)
	return sort_words(words)

def first_and_last(sentence):
	""" print first and last words of the sentence."""
	words= break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	""" sort the words and then print first and last one."""
	words=sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


