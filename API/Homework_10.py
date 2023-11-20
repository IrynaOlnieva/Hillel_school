# Написати тести на створювання користувача, та логін у систему.
# Тест на перевірку профіля користувача
# Написати параметризований тест, на перевірку реєстрації з правильними та неправильними паролями

# import requests
import pytest
import requests

class UserSingUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password


user = UserSingUpModel("John", "Dou", "test77777@test.com", "Qwerty12345", "Qwerty12345")

session = requests.session()
get_current_user = session.get("https://qauto2.forstudy.space/api/users/profile")
post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user.__dict__)
print(get_current_user.text,get_current_user.status_code)
print(post_new_user.text,post_new_user.status_code)

users = [
    ("John", "Doe", "test77777@test.com", "Qwerty12345", "Qwerty12345"),
    ("John", "Doe", "test77777g@test.com", "Qwerty123456", "Qwerty123456"),
]

@pytest.mark.parametrize("name, last_name, email, password, repeat_password", users)
def test_register_user(name, last_name, email, password, repeat_password):
    test_dic = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    session = requests.session()
    post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json = test_dic )

    assert post_new_user.status_code == 201