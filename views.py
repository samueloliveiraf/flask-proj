from werkzeug.security import generate_password_hash, check_password_hash
from decouple import config

from flask_httpauth import HTTPBasicAuth


users = {
    config('USER_NAME'): generate_password_hash(config('USER_PASSWD'))
}

auth = HTTPBasicAuth()


def validate_cnpj(cnpj):
    cnpj = ''.join(c for c in cnpj if c.isdigit())
    if len(cnpj) != 14:
        return False

    def calculate_digit(cnpj, digit):
        if digit == 1:
            weights = list(range(5, 1, -1)) + list(range(9, 1, -1))
            mod = 11
        elif digit == 2:
            weights = list(range(6, 1, -1)) + list(range(9, 1, -1))
            mod = 11
        sum_ = sum([int(cnpj[i])*weights[i] for i in range(len(weights))])
        rest_division = sum_ % mod
        return 0 if rest_division < 2 else mod - rest_division

    first_digit = calculate_digit(cnpj, 1)
    second_digit = calculate_digit(cnpj, 2)

    return cnpj[-2:] == "{0}{1}".format(first_digit, second_digit)


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
