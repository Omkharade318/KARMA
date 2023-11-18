from bardapi import BardCookies
import datetime

cookie_dict={
    "__Secure-1PSID" : "dAjjSvL07uQ4hcJQrjK3hEIpIK36ctHqUwXK2Y4tCpZqrvWgGYd_n1ntKJuxb9jlCIdwFw.",
    "__Secure-1PSIDTS" : "sidts-CjEBNiGH7q5mF7mPUvJ4V28iXtQRXoO4HD1jx1ezAmfFnV19BG2U-RbsbZwSj4nDoCVnEAA",
    "__Secure-1PSIDCC" : "ACA-OxOaXYchG7xmUy7vRRtPe-RMEhTv9wstGLfeobBi3EdykIZs_nV5hBgKcZOrNBGaZVQFGhY"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Enter your Query: ")
    Reply = bard.get_answer(Query)['content']
    print(Reply)