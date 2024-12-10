def main():
    theText = '''
       Python was conceived in the late 1980’s by Netherlands programmer
    Guido Van Rossum and rolled out in 1991. Developing the language
    was a hobby project for Van Rossum to keep him occupied over
    Christmas, though he soon began implementing the language at
    his employer Centrum Wiskunde & Informatica (CWI). The name of
    the language was inspired by Monty Python’s Flying Circus, and
    today users of this code often work in references to Monty Python.
    Python is one of the most popular programming languages in the
    world. As a scripting language that can automate a complex series
    of tasks, Python is used on the back end of many web applications,
    games, and digital and animated special effects. Sites like YouTube
    and Instagram are among some of the titans that rely on this
    language to support both front-end and back-end functionality.    
    '''
    print("Original Text:")
    print(theText)
    originalLength = len(theText)
    print("\nOriginal Length: ", originalLength)
    trimmedText = theText.strip()
    print("\nText after removing leading and trailing spaces:")
    print(trimmedText)
    newLength = len(trimmedText)
    print("\nNew Length after removing spaces: ", newLength)
    theCount = trimmedText.lower().split().count('the')
    print("\nCount of 'the': ", theCount)
    if 'little' in trimmedText.lower():
        print("\n'Little' is found in the text.")
    else:
        print("\n'Little' is not found in the text.")
    if 'titan' in trimmedText.lower():
        print("\n'Titan' is found in the text.")
    else:
        print("\n'Titan' is not found in the text.")
    positionOfAppl = theText.find('appl')
    print("\nPosition of 'appl': ", positionOfAppl)
    theText2 = theText
    theText2 = theText2.replace('Python', 'PYTHON')
    print("\nUpdated Text after replacing 'Python' with 'PYTHON':")
    print(theText2)

main()
