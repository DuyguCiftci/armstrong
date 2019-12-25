text = """
Armstrong Number Control
"""
print(text)

num = input("Enter the number: ")
num_digit = len(num)
num = int(num)
digit = 0
summ = 0
temp = num

while temp > 0: 
    digit = temp % 10
    summ += (temp%10)**num_digit
    temp //= 10

if summ == num:  
   print(num,"is an Armstrong number.")  
else:  
   print(num,"is not an Armstrong number.") 



