def get_soundex_code(char):
    """
    Returns the Soundex code for the given character.
    """
    return {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }.get(char.upper(), '0')
 
def generate_soundex(name):
    """
    Generates the Soundex code for the given name.
    """
    return name[0].upper() + ''.join(get_soundex_code(char) for char in name[1:])[:3].ljust(4, '0')
