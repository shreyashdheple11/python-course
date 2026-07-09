# # # count = 0 
# # # while count < 20:
# # #     print('hi,  i am shreyash')
# # #     count = count + 2

# # x = 5
# # while x > 0:
# #     print(x)
# #     x = x - 1

# answer = " "
# while answer != "quit":
#     answer = input('Type somwthing:')
#     print("You Typed: ", answer)
# else:
#     print("Program terminated Success !")

sport_lst = ["Cricket", "Football", "Badminton", "Rugby", "Tennnis", "Volleyball",
 "carrom", "chess", "running"]
lst_len = len(sport_lst)
index = 0
while index < lst_len:
    if sport_lst[index] == "Rugby":
        print('Rugby is available')
        break
    index += 1
else:
    print('Rugby isnt available')