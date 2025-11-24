import re
import base64

def parse_bat_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    variables = {}
    order_line = ""

    # Regex to match the set lines
    # Pattern: !qoz! (junk)char(junk)char... = value
    # We can just look for lines starting with !qoz!
    
    for line in lines:
        line = line.strip()
        if line.startswith("!qoz!"):
            # Check if it's a variable assignment or the final execution lines
            if "=" in line:
                parts = line.split("=")
                lhs = parts[0]
                rhs = "=".join(parts[1:]) # In case value has =
                
                # Extract variable name from lhs
                # lhs looks like "!qoz! %FTW%b%FTW%y%FTW%o%FTW%"
                # We want "byo"
                # Remove "!qoz!"
                lhs = lhs.replace("!qoz!", "").strip()
                
                # Remove %...% blocks
                # We can just remove anything between % and % including the %s
                # But wait, the characters we want are OUTSIDE the %...%?
                # No, look at line 15: %FTW%b%FTW%y%FTW%o%FTW%
                # The 'b' is between %FTW% and %FTW%?
                # No, it's %FTW% b %FTW% y %FTW% o %FTW%
                # So we just need to remove all %.*?% sequences?
                # Let's try removing all %...% sequences.
                
                clean_lhs = re.sub(r'%[^%]*%', '', lhs)
                variables[clean_lhs] = rhs.strip()
        
        elif line.startswith("%") and line.endswith("%"):
            # This might be the order line (line 125)
            # It contains many %var% sequences
            if len(line) > 100: # Heuristic
                order_line = line

    if not order_line:
        print("Could not find order line")
        return

    # Extract variable names from order line
    # They are like %qdu%%ssf%...
    # So we split by % and take every other item?
    # %qdu% -> empty, qdu, empty
    # %qdu%%ssf% -> empty, qdu, empty, ssf, empty
    
    # Or just findall %([^%]*)%
    ordered_vars = re.findall(r'%([^%]*)%', order_line)
    
    full_string = ""
    for var in ordered_vars:
        if var in variables:
            full_string += variables[var]
        else:
            print(f"Variable {var} not found!")

    # Remove the junk string
    # The junk string 'djlrttmeqqkr' is mentioned in the file
    clean_string = full_string.replace('djlrttmeqqkr', '')
    
    print(f"Clean string length: {len(clean_string)}")
    
    with open("clean_command.txt", "w") as f:
        f.write(clean_string)
        
    print("Saved clean command to clean_command.txt")
    
    # Try to find the base64 part
    # It usually follows -EncodedCommand or similar, or is assigned to a variable in the PS command
    # Looking at the raw file, line 40 says: $oddCount / $oddZeroRatio -ge 0.5
    # Line 39 says: [Convert]::FromBase64String($s)
    # So there is a variable $s that contains the base64.
    
    # Let's just print the whole thing for now so I can inspect it.
    print(clean_string)

parse_bat_file('/home/jait-chd/.gemini/antigravity/scratch/manual_challenge/tradesman_manual.bat')
