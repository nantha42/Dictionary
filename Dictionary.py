from nltk.corpus import wordnet as wn 

def Word(word = ''):
	if(word == ''):
		word = raw_input()
			
	print("\nPlease wait...\n")
	words = wn.synsets(word)
	print"\nDefinitions:"
	for node in words:
		if(word in node.name()):
			print(node.name()+":       "+node.definition())
	

	print"\nRelated Words:"
	related_w = []
	for node in words:
		for node_name in node.lemma_names():
			if node_name not in related_w:
				related_w.append(node_name)
	print(related_w)
	
		


if __name__ == '__main__':
	print("\nEnter the word:")
	Word()


