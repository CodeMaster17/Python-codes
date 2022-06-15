num = input("Enter the number : ");
num = int(num);
i = 1;
c = 0;
while i <= num:
    if(num % i == 0):
        c += 1;
    i += 1;

if( c == 2):
    print("It is a prime number");

else:
    print("It is a composite  number");