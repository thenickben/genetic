def fitness (password, test_word):
	
	if (len(test_word) != len(password)):
		print("taille incompatible")
		return
	else:
		score = 0
		i = 0
		while (i < len(password)):
			if (password[i] == test_word[i]):
				score+=1
			i+=1
		return score * 100 / len(password)