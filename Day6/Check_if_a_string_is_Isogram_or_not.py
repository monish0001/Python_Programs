class isogram:
    def check_isogram(self, string):
        string = string.lower()
        char_set = set()
        for char in string:
            if char.isalpha():  # Consider only alphabetic characters
                if char in char_set:
                    return False
                char_set.add(char)
        return True
    
# Example usage:
if __name__ == "__main__":
    iso = isogram()
    test_string = "Dermatoglyphics"
    if iso.check_isogram(test_string):
        print(f'"{test_string}" is an isogram.')
    else:
        print(f'"{test_string}" is not an isogram.')