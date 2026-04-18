def decrypt_result(s):
    # Positive result
    if s == "1" or s == "4" or s == "78":
        return "+"
    
    elif s.endswith("35"):
        return "-"
    
    elif s.startswith("9") and s.endswith("4"):
        return "*"
    
    elif s.startswith("190"):
        return "?"
    
    return "?"

s1=["78",
"7835",
"19078",
"944"]

for c in s1:
    print(decrypt_result(c))
