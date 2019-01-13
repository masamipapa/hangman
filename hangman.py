def hangman(word):
	wrong = 0
	stages = ["",
			  "_________            ",
			  "|                    ",
			  "|      |      ",
			  "|      0      ",
			  "|     /|\     ",
			  "|     / \     ",
			  "              "
			  ]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("ハングマンへようこそ！")
	while wrong < len(stages) - 1:
		print("\n")
		msg = "１文字を予想してね"
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board(cind) = char
			rletters[cind] = 's'
		else:
			wrong += 1
		print(" ".join(board))
		e = wrong + 1
		print("\n".join(stages[0:e]))
			print("あなたの勝ち！")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("あなたの負け！正解は、{}.".format(word)

hangman("cat")
