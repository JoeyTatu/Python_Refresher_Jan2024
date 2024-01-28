# 數字 = 23
# 運行 = 真
# 當 運行:
#     猜測 = 整數(輸入("Enter an integer : ")

#     如果 猜測 == 數字:
#         印出("Congratulations, you guessed it.")
#         運行 = 假 # 這會讓循環語句結束
#     假使 猜測 < 數字:
#         印出("No, it is higher than that.")
#     否則:
#         印出("No, it is lower than that.")
# 否則:
#     印出("The while loop is over")
# 印出("Done")

number = 23
running = True
while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        running = False # this causes the while loop to stop
    elif guess < number:
        print('No, it is higher than that.')
    else:
        print('No, it is lower than that.')
else:
    print('The while loop is over')
print('Done')