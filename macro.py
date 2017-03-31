'''Program used to calculate an ectomporph's suggested daily macronutrients'''

from time import sleep

def main():
	name = input('What is your name? ')
	print('Hello ', name)
	weight = float(input('What is your weight? '))
	if weight > 300:
		print('Go eat a salad')
	else:
		print("OK, your'e not that fat.")
	height = float(input('How tall are you?, List in inches. '))
	age = float(input('Awesome! And how old are you? '))
	print('Got it! Computing your metabolic rate right now...')
	global metabolic_rate
	metabolic_rate = 66 + (6.23 * weight) + (12.7 * height) - (6.76 * age)
	sleep(3)
	print("Ok",name,", you're metabolic rate is: ", format(metabolic_rate, '.2f'))
	result_mb = input('Do you know what this means? Y/N ')
	if result_mb == 'Y':
		print('Ok look at you!')
	else:
		print("You're metabolic rate means you will lose", format(metabolic_rate, '.2f'), "calories a day even if you don't do anything physical.")
	sleep(2)
	findCalories()		

def findCalories():
	result_cal = input('Do you want to find out how many calories you should eat per day? Y/N ')
	if result_cal == "Y":
		print("Great! Let's start.")
	else:
		print("Then go to Mcdonalds fatty!")
	sleep(2)
	activity_rates = {'LE' : 1.2, 'ME': 1.5, 'HE' : 1.8}
	activity_levels = {'Light Exercise' : 'LE', 'Moderate Exercise': 'ME', 'Heavy Exercise' : 'HE'}
	print('\n')
	for level in activity_levels:
		print(level, activity_levels[level])
	print('\n')	
	userLvl = input('Select the activity level that best describes your weekly workouts by typing in the 2 digit code next to the desired level. ')
	for rate in activity_rates:
		if userLvl == rate:
			print('Got it! Calculating Results...')
			sleep(2)
			userCal = metabolic_rate * activity_rates[rate]
			print('You can eat ', format(userCal, '.2f'), "calories a day and will not gain weight!")
			break
		else:
			continue
	print("Now let's calculate your daily macronutrients intake!")
	sleep(3)
	findMacro()

def findMacro():
	print("What is your goal?")
	print("\n")
	reasons = {'gain weight' : 1, 'lose weight' : 2}
	percentages = {1 : "55%% carbs 25%% protein 20%% fat", 2 : "40%% carbs 35%% protein 25%% fat"}
	for reason in reasons:
		print(reason, reasons[reason] )
	print("Select your goal by typing in the number")	
	user_reason = int(input("associated with your goal "))
	for reason in reasons:
		if user_reason == reasons[reason]:
			for percentage in percentages:
				if user_reason == percentage:
					print("In order to ", reason", your macronutrients percentages should be:")
					print(percentages[user_reason])

if __name__ == '__main__':
	main()