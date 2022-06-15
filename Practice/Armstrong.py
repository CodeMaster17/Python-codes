num = input("enter the number");
num1 = int(num);
num = int(num);
sum = 0;
while num > 0:
    rem = int(num % 10);
    sum = sum + (rem * rem * rem);
    num /= 10;

# to print a sentence and a number together
print("The sum is" , sum);

if( sum == num1):
    print("This is a Armstrong Number");

else:
    print("This is not a Armstrong number");
