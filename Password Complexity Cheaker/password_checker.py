import re


def password_checker ():
    score = 0
    password = input(str("Enter password: "))

    blacklist = ["Password@123", "P@ssw0rd1123", "Admin#01"]
    if password in blacklist:
        score == 0
        print("  >>>This is commonly used password, Please change it.")

    if len(password) >= 8:
        score += 1
    else:
        print("    >>>Increase the length to 8 characters or more")

    if re.search(r"[0123456789]", password):
        score += 1
    else: 
        print("    >>>Add at least one number")

    if re.search(r"[!@#$%^&*(),.?':{}|<>]", password):
        score += 1
    else:
        print("    >>>Add at special character")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("    >>>Ensure the password has lowercase letter")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("    >>>Ensure the password has uppercase letter")


    if score == 1 :
        print("######## Final Verdict: Password is Weak  ########")

    elif score == 2:
        print("######## Final Verdict: Password is Weak  ########")

    elif score == 3:
        print("######## Final Verdict: Password is Moderate ########")

    elif score == 4:
        print("######## Final Verdict: Password is Moderate ########")

    elif score == 5:
        print("######## FINAL VERDICT: Password is Strong ########")
        
 
print ("################ PASSWORD COMPLEXITY CHECKER ################")
print ("""*Password must have at least 8 characters 
*Password must at least have a uppercase letter
*Password must at least have a lowercase leter 
*Password must include numbers
*Password must include symbols (e.g.,!@#$%_?)""")


password_checker ()
