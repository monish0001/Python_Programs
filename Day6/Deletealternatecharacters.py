class deleteAlternateCharacters:
    def delete_alternate(self, s: str):
        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(s[i])
        return ''.join(result)
    
# Example usage:
if __name__ == "__main__":
    deleter = deleteAlternateCharacters()
    test_string = "abcdefg"
    modified_string = deleter.delete_alternate(test_string)
    print(f'Original string: "{test_string}"')
    print(f'String after deleting alternate characters: "{modified_string}"')