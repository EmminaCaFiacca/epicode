import random
import string

def genera_password(complessa=False):
    
    if complessa:
        caratteri = string.ascii_letters + string.digits + string.punctuation
        lunghezza = 20
    else:
        caratteri = string.ascii_letters + string.digits

    return "".join(random.choice(caratteri) for _ in range(20 if complessa else 8))


print("Password semplice (8 caratteri):", genera_password(complessa=False))
print("Password complessa (20 caratteri):", genera_password(complessa=True))