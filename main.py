num_list = list(range(1,101))
for x in num_list:
    if x%3 == 0:
        print("Fizz")
    elif x%5 ==0:
        print('Buzz')
    elif x%3 and x%5:
        print("FizzBuzz")
    print(x)