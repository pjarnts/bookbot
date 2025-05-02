def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def get_sorted_chars(char_dict):
    def sort_on(char_dict):
        return char_dict["num"]
    sorted_list = []
    for char in char_dict:
        sorted_list.append(
            {
                "char": char,
                "num": char_dict[char]
            }
        )
    sorted_list.sort(reverse= True, key=sort_on)
    return sorted_list

