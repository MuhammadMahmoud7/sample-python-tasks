def Calc_Grade(grade):
	if grade >=0 and grade <=100 :
		if grade >=90 :
			print("A")
		elif grade >=80 :
			print("B")
		elif grade >=70 :
			print("C")
		elif grade >=60 :
			print("D")
		else :
			print("F")
	else :
		print("Sorry your Grade is out of range ! Minimum Grade is 0 and Maximum grade is 100 ")
								


grade = int(input("Enter a student grade: "))

Calc_Grade(grade)				
