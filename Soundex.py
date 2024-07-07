def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 
        'C': '2', 'G': '2', 
        'D': '3', 'T': '3',
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

soundex = name
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
