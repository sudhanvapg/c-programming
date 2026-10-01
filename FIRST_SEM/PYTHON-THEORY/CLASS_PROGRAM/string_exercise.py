#Program to demonstrate real python string processing to clean and transform
# Output formate:
# ==============================
#  PROFILE CARD
# ==============================
#  Name     : Naveen Kumar
#  Initials : NK
#  Email    : naveen.kumar@company.com
#  Domain   : company.com
#  Phone    : *********3210
#  Valid    : True
# ==============================

raw_data = """
   naveen   KUMARṇ
naveen.kumar@COMPANY.com
+91-98765-43210
"""
###@@@
name,email,phone=raw_data.split("\n")[1],raw_data.split("\n")[2],raw_data.split("\n")[3]
print(name.strip().title())
print(email)
print(phone.replace("-",""))

first,last=name.split()[0],name.split()[1]
initials=first[0].upper()+last[0].upper()
###@@@



# Splitting rows by newline and removing empty edge items
lines = [line.strip() for line in raw_data.strip().split("\n")]
name_raw, email_raw, phone_raw = lines[0], lines[1], lines[2]

# 1. Process Name & Initials
name = name_raw.title()
name_parts = name_raw.split()
initials = (name_parts[0][0] + name_parts[1][0]).upper() if len(name_parts) >= 2 else ""

# 2. Process Email & Domain
email = email_raw.lower()
domain = email.split("@")[1] if "@" in email else ""

# 3. Process Phone Number masking (keeping last 4 digits)
clean_phone = phone_raw.replace("-", "")
masked_phone = "*" * (len(clean_phone) - 4) + clean_phone[-4:]

# 4. Validation Check
is_valid = "@" in email and len(clean_phone) >= 10

# Print Formatted Output
print("==============================")
print("PROFILE CARD")
print("==============================")
print(f"Name     : {name}")
print(f"Initials : {initials}")
print(f"Email    : {email}")
print(f"Domain   : {domain}")
print(f"Phone    : {masked_phone}")
print(f"Valid    : {is_valid}")
print("==============================")