raw_data = """ naveen KUMAR
  naveen.kumar@COMPANY.com
+91-98765-43210
"""
lines = raw_data.strip().splitlines()
name = lines[0].strip()
email = lines[1].strip()
phone = lines[2].strip()

name = " ".join(word.capitalize() for word in name.split())
initials = "".join(word[0].upper() for word in name.split())
email = email.lower()
domain = email.split("@")[1]
phone_digits = "".join(char for char in phone if char.isdigit())
valid = phone_digits.startswith("91") and len(phone_digits) == 12
masked_phone = "*" * (len(phone_digits) - 4) + phone_digits[-4:]

print("Name     :", name)
print("Initials :", initials)
print("Email    :", email)
print("Domain   :", domain)
print("Phone    :", masked_phone)
print("Valid    :", valid)