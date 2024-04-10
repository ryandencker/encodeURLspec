import sys

def encoder(instring):
    modified_string = instring.replace('"', '%22')
    modified_string = modified_string.replace(':', '%3A')
    modified_string = modified_string.replace('<', '%3C')
    modified_string = modified_string.replace('>', '%3E')
    modified_string = modified_string.replace('/', '%2F')
    modified_string = modified_string.replace(' ', '+')
    modified_string = modified_string.replace('?', '%3F')
    modified_string = modified_string.replace('{', '%7B')
    modified_string = modified_string.replace('}', '%7D')
    modified_string = modified_string.replace('(', '%28')
    modified_string = modified_string.replace(')', '%29')
    modified_string = modified_string.replace("'", '%27')
    modified_string = modified_string.replace('=', '%3D')
    modified_string = modified_string.replace('&', '%26')
    modified_string = modified_string.replace(';', '%3b')
    modified_string = modified_string.replace('%', '%25')
    return modified_string

if __name__ == "__main__":
    #if len(sys.argv) != 2:
     #   print("Usage: python encodeURLspec.py <string>")
      #  sys.exit(1)
    instring = input("Please paste your string: ")   
#instring = sys.argv[1]

    modified_string = encoder(instring)

    print("\nHere is encoded output:\n")
    print(modified_string)