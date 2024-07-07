soundex = name.upper()
prev_code = get_soundex_code(soundex)
 
for char in name[1:]:
    code = get_soundex_code(char)
    if code != '0' and code != prev_code:
        soundex += code
        prev_code = code
    if len(soundex) == 4:
        break
 
# Pad with zeros if necessary
soundex = soundex.ljust(4, '0')
 
return soundex
