# функція зворотнього виклику

def new():  # callback func
    pass


def callback(phone):  # в тілі цієї функції викликається z z колбек функція
    phone()


callback(new) 


def print_numb_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered numb is odd")


def process_number(num, callback_fn):  # Без різниці, що робить callback_fn, їй передається число num
    callback_fn(num)


entered_num = int(input("Enter any number: "))

process_number(entered_num, print_numb_info)


