import requests
# test_dict = {
#   "name": "John",
#   "lastName": "Dou",
#   "email": "testjgujhhfyfikhhhki@test.com",
#   "password": "Qwerty12345",
#   "repeatPassword": "Qwerty12345"
# }
# #
# # get_current_user = requests.get("https://qauto2.forstudy.space/api/users/current")
# # post_new_user = requests.post(url="https://qauto2.forstudy.space/api/auth/signup", json=test_dict)
# # print(get_current_user.text)
# # print(post_new_user.text)
#
# session = requests.session()
#
# get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
# post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=test_dict)
# get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
# print(get_current_user.text)
# print(post_new_user.text)
# print(get_current_user_after_post.text)

# class UserSignModel:
#   def __init__(self,name, last_name, email, password, repeat_password):
#     self.name = name
#     self.LastName = last_name
#     self.email = email
#     self.password = password
#     self.repeatPassword = repeat_password

# user_to_sing_up = UserSignModel("John", "Dou", "testjsddgkjhhikhki@test.com","Qwerty12345","Qwerty12345")
#
# session = requests.session()
#
# get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
# post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_to_sing_up.__dict__)
# get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
# print(get_current_user.text)
# print(post_new_user.text)
# print(get_current_user_after_post.text)


class UserSignModel:
  def __init__(self,name, last_name, email, password, repeat_password):
    self.name = name
    self.LastName = last_name
    self.email = email
    self.password = password
    self.repeatPassword = repeat_password

class TestRegistration:
  def setap_class(self):
     self.user_to_sing_up = UserSignModel("John", "Dou", "testrtr71j@test.com", "Qwerty12345", "Qwerty12345")

  def setup_method(self):
    self.session = requests.session()

  def test_check_successful_user_registration(self):
    post_new_user = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_to_sing_up.__dict__)
    assert post_new_user.status_code == 201


  def test_check_successful_user_registration1(self):
    post_new_user = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_to_sing_up.__dict__)
    assert post_new_user.status_code == 201



  def teardown_method(self):
    self.session.delete("https://qauto2.forstudy.space/api/users")