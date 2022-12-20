print('---------------------------------------------------')
print("-------Welcome to Salary Calculater!---------------")
print('---------------------------------------------------')
Base_salary=int(input('Enter Your Basic Salary per Month:'))
Month_sales=int(input('Enter Your Sales in Doller in this Month:'))
if Month_sales <= 1000:
  total_salary=Base_salary
  print('Sorry! you are not eligible for bonus.Work more to get more bonus!,Your total salary ofthis month is {0}'.format(total_salary))
elif Month_sales > 1000 and Month_sales <= 2000:
  total_salary=Base_salary+50
  print('Congratulations!,You are eligible to get bonus ${0} and your total salary ofthis month is {1}'.format(50,total_salary))
elif Month_sales > 2000 and Month_sales <= 5000:
  total_salary=Base_salary+100
  print('Congratulations!,You are eligible to get bonus ${0} and your total salary ofthis month is {1}'.format(100,total_salary))
elif Month_sales > 5000 :
  total_salary=Base_salary+150
  print('Congratulations!,You are eligible to get bonus ${0} and your total salary ofthis month is {1}'.format(150,total_salary))
