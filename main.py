def main():
    text = read_book_from_file()
    dict = count_letters(text)
    print_report(dict)

def read_book_from_file():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text

def get_word_count(text: str):
    l = len(text.split())
    print(l)

def count_letters(text: str):
    # we don't care about case
    lowered = text.lower()
    dict = {}
    for t in lowered:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    # print(dict)
    return dict

def print_report(dict: dict):
    # create a list
    list = []
    for d in dict:
        list.append({"char": d, "count": dict[d]})
    
    def sort_on(dict):
        return dict["count"]

    list.sort(reverse=True, key=sort_on)

    for i in range(0, len(list)):
        if list[i]["char"].isalpha():
            print(f"The '{list[i]["char"]}' character was found {list[i]["count"]} times")
    



main()