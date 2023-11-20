import pytest
# def test_check_sum():
#     assert 10 == 10
#
# @pytest.mark.parametrize("first_num, second_num,expected_sum",[(1,2,3),(2,2,4),(5,5,10)])
# def test_check_sum_test(first_num,second_num, expected_sum):
#     assert custom_sum(first_num, second_num) == expected_sum
#
# def custom_sum(first_num, second_num):
#     return first_num + second_num

# @pytest.mark.parametrize("name, last_name,email,password,repeat_password",[('John','Dou','test1666@test.com','Qwerty12345','Qwerty12345')])
# def test_check_sum_test(name, last_name, email, password, repeat_password):
#     test_dict = {
#         "name": name,
#         "last_name": last_name,
#         "email": email,
#         "password": password,
#         "repeat_password": repeat_password
#     }
#
#
#     # session = requests.session()
#      post_new_user = requests.post(url="https://qauto2.forstudy.space/api/auth/signup", json=test_dict)
#
#     assert post_new_user.status_code == 200






ser_data = [
    ("John", "Doe", "johdoe@e11xample.com", "Qwerty12345", "Qwerty12345"),
    ("Jane", "Smith", "janesmith@e11xample.com", "Qwerty12345", "Qwerty12345"),
    ("", "Johnson", "john.johnson@example.com", "password789", "password789"),
]

@pytest.mark.parametrize("name, last_name, email, password, repeat_password",ser_data)
def test_register_user(name, last_name, email, password, repeat_password):
    test_dict = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    session = requests.session()
    post_new_user = requests.post(url="https://qauto2.forstudy.space/api/auth/signup", json=test_dict)

    assert post_new_user.status_code == 201
