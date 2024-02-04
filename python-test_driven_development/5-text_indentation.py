def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = text
    for delimiter in "?:.":
        result = (delimiter + "\n\n").join(
            [index.strip() for index in result.split(delimiter)])

    print("Actual stdout:", result)
    return result
