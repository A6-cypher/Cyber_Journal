#Read the number between 1 to 10 and then print it in words

num=eval(input("Enter a number: "))

num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

if num in [1,2,3,4,5,6,7,8,9,10]:
    print("Converting your number into a word....")
    print(num_word.get(num))
else:
    print(f'Your number {num} is not in the range of 1 to 10.')