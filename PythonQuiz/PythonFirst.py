#
# number_of_entries = int(input('please enter the num of numbers:'))
#
# i = 0
# sum = 0
# count = number_of_entries
# average = 0
# num_count_str = 0
#
# while count > 0:
#     num_count_str = str(i + 1)
#     num_print = float(input('please enter the ' + num_count_str + 'th' + ' number:'))
#     count = count - 1
#     i = i + 1
#     sum = sum + num_print
#     average = sum / i
#     print('The average num is:' + str(average))




#
# number_of_entries = int(input('please enter the num of numbers:'))
#
# i = 0
# sum = 0
# count = number_of_entries
# average = 0
# num_count_str = 0
#
# while count > 0:
#     num_count_str = str(i + 1)
#     num_print = float(input('please enter the ' + num_count_str + 'th' + ' number:'))
#     count = count - 1
#     i = i + 1
#     sum = sum + num_print
#     average = sum / i
#
# print('The average num is:' + str(average))





number_of_entries = int(input('please enter the num of numbers:'))

i = 0
sum = 0
count = number_of_entries
average = 0

while count > 0:
    num_print_str = str(input('please enter the ' + str(i + 1) + ' number:'))
    if num_print_str == "":
        break

    num_print = float(num_print_str)

    count = count - 1
    i = i + 1
    sum = sum + num_print
    average = sum / i

print('The average num is:' + str(average))

