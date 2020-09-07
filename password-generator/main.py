from valid_password_generator import *

attempts = 0
valid = False
while not valid:
    psw = password_generator()
    print(psw)
    if password_validate(psw):
        valid = True
        attempts += 1
    else:
        attempts += 1
print("-------------------------------------")
print(f'La contraseña {psw} es correcta.')
print(f'Intentos: {attempts}')
