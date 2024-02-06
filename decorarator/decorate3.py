# Перевірка авторизаціїкористувача

def is_user_authenticated():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            print("User is NOT authenticated")
            raise Exception("user is not authenticated")
    

    return wrapper


@check_user_auth
def do_sensitive_job():  # В тілі цієї функції буде виконуватися дія у тому випадку, якщо користувач вже авторазований
    #Do some tasks only if user is authenticated
    print("Results of some sensitive tasks")



do_sensitive_job()