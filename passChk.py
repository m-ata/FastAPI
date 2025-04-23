

password = str(input("Enter you password : "))
length_pass = len(password)

status = "Strong" if length_pass > 8 else "Weak"
print("Your Password : ", password)
print("Password Strength : ", status)

