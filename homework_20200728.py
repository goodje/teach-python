def even(additional):
    # even_tuple = (2, 4, 6, 8, 10)
    even_list = [2, 4, 6, 8, 10]
    result = even_list[0] + (even_list[1] + even_list[2]) * (even_list[3] - even_list[4]) - additional
    return result

def mathFunction(num_list, additional):
    # for number in num_list:
    return num_list[0] + (num_list[1]+num_list[2]) * (num_list[3]-num_list[4]) - additional

if __name__ == "__main__":
    add = 12
    print(even(add))

    # num_list = [1,2,3,4,5]
    # add = 6
    # print(mathFunction(num_list, add))

