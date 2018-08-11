from urllib.request import urlopen

def fetch_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
		    line_words = line.decode('utf-8').split()
		    for word in line_words:
		    	story_words.append(word)
		    
	for word in story_words:
		print(word)

#print(__name__).  --It will print the __main__
if __name__ == '__main__': #Used __name__ to determine how the module is used.
	fetch_words()
