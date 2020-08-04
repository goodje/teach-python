def check_qualified(name):
    score = {
        'jim': {'maths': 8, 'english': 4},  # out of 10
        'harry': {'maths': 3, 'english': 4},
        'larry': {'maths': 8, 'english': 8}
    }

    qualification_score = 7
    # TODO rewrite it using or or and
    if score[name]['maths'] >= qualification_score:
        print(name + ' is qualified to graduate')
    elif score[name]['english'] >= qualification_score:
        print(name + ' is qualified to graduate')
    else:
        print(name + ' is not qualified to graduate')


if __name__ == '__main__':

    # print(8 >= 6 or False)
    # print(True and True)
    # print(True and False)
    # print(False and False)
    # print(3 >= 6 and 4 >= 6)
    # exit()
    # either >=6 is qualified to graduate
    # both >=6 is to be awarded
    # who will be qualified to graduate
    name = 'jim'
    check_qualified(name)

    check_qualified('harry')

    # who will be awarded HOMEWORK
    # print("to be awarded")
