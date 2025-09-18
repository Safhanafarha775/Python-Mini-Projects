
def calculate_bmi(h,w):
	h_in_m=float(h/100)
	bmi=w/(h_in_m**2)
	if bmi<18.5:
		status='Underweight'
	elif 18.5<bmi<24.9:
		status='Normal'
	elif 24.9<bmi<29.9:
		status='Overweight'
	else:
		status='Obese'
	print("BMI = ",round(bmi,2))
	print('Status : ',status)
	
weight=float(input("Enter your weight in kgs : "))
height=float(input("Enter your height in cms : "))
calculate_bmi(height,weight)
