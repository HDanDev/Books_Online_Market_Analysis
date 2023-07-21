import re

def safeFilename(string):
    max_length = 30
    cleaned_filename = (
        re.sub(r'[^a-zA-Z0-9_]', '', string.replace(" ", "_"))
    ).strip()

    if len(cleaned_filename) > max_length:        
        return cleaned_filename[:max_length] + "_etc"

    return cleaned_filename
