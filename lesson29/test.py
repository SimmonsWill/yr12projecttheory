
# Return true or false
# Check if username valid
# 3-12 letters
# must begin with a letter
def valid_username(name):
    if not name[0].isalpha():
        return False
    return 3 <= len(name)



