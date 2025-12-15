num_list = list(range(1,101))
for x in num_list:
    if x%3==0 and x%5==0:
        print("FizzBuzz", x)
    elif x%5 ==0:
            print('Buzz',x)
    elif x%3 == 0:
            print("Fizz",x)
    else:
        print(x)
        