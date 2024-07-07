def get_soundex_code(char):
    """
    Returns the Soundex code for the given character.
    """
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(char.upper(), '0')
 
def generate_soundex(name):
    """
    Generates the Soundex code for the given name.
    """
    if not name:
        return ""
 
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
 
    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        if len(soundex) == 4:
            break
 
    if len(soundex) < 4:
        soundex = soundex.ljust(4, '0')
 
    return soundex
