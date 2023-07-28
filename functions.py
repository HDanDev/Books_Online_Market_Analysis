import re

def safeFilename(string):
    maxLength = 30
    cleanedFilename = (
        re.sub(r'[^a-zA-Z0-9_]', '', string.replace(" ", "_"))
    ).strip()

    if len(cleanedFilename) > maxLength:        
        return cleanedFilename[:maxLength] + "_etc"

    return cleanedFilename

def urlCleaner(string, expressionToRemove, newExpression):
    regex = re.escape(expressionToRemove)
    
    newString = re.sub(regex, newExpression, string)
    
    return newString