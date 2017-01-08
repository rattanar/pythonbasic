def find_next_word(text, word, start_pos) :
	word_pos = text.find(word, start_pos)
	if (word_pos != -1):
		text = text[word_pos+len(word)+1:]
		if(text.find(" ") !=-1):
			next_word = text[: text.find(" ")]
			start_pos = text.find(" ")+1
		else:
			next_word = text
			start_pos = -1
		print(next_word)
		return text, start_pos
	else:
		print("")
		return"",-1



