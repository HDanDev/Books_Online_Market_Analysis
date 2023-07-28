import re

def safeFilename(string):
    max_length = 30
    cleanedFilename = (
        re.sub(r'[^a-zA-Z0-9_]', '', string.replace(" ", "_"))
    ).strip()

    if len(cleanedFilename) > max_length:        
        return cleanedFilename[:max_length] + "_etc"

    return cleanedFilename
