original_password = "contraseña"
password = input("Introduce la contraseña: ")
if original_password == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")