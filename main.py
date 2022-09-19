#find the smallest numnber among three integers
number1_ = int(input("Enter number1_"))
number2_ = int(input("Enter number2_"))
number3_ = int(input("Enter number3_"))
if (int(number1_)) > (int(number2_)) > (int(number3_)):
  print ("(number3_) is the smallest number")
if (int(number1_)) < (int(number2_)) < (int(number3_)):
 print ("(number1_) is the smallest number")
if (int(number2_) < int(number1_) < int(number3_)):
  print ("(number2_) is the smallest number")
elif (int(number1_) == int(number2_) < int(number3_)):
  print ("(number1_) and (number2_) are the smallest numbers")
elif (int(number2_) == int(number3_) < int(number1_)):
  print ("(number2_) and (number3_) are the smallest numbers")
elif (int(number1_) == int(number3_) < int(number2_)):
  print ("(number1_) and (number3_) are the smallest numbers")
