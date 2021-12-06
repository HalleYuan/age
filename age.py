drive = input('請問你有沒有開過車?')
if drive != '有' and drive != '沒有':
    print('只能輸入 有/沒有')	
    raise SystemExit
    
age = input('請問你的年齡?')
age = int(age)
if drive == '有':
    if age >= 18:
    	print('恭喜，你通過測驗了!')
    else:
    	print('奇怪...你怎麼會有開過車咧?')
elif drive == '沒有':
	if age >= 18:
		print('你可以考駕照了，怎麼還不趕快去考?')
	else:
		print('沒關係，再過幾年就可以考了')