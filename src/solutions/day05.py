from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    rules = []
    books = []
    for line in data[0].split('\n'):
        rules.append(tuple(map(int, line.split('|'))))
    for line in data[1].split('\n'):
        books.append(list(map(int, line.split(","))))
    return rules, books


def already_ordered(rules, books):
    correct_idx = []
    for i, pages in enumerate(books):
        correct = True
        for rule in rules:
            if rule[0] in pages and rule[1] in pages:
                idx0, idx1 = pages.index(rule[0]), pages.index(rule[1])
                if idx0 > idx1:
                    correct = False
        if correct:
            correct_idx.append(i)

    middle_sum = 0
    for idx in correct_idx:
        book = books[idx]
        middle_sum += book[len(book)//2]        

    return middle_sum, correct_idx


def order_pages(rules, books, correct_idx):
    for i, pages in enumerate(books):
        correct = False
        while not correct:
            changed = False
            for rule in rules:
                if rule[0] in pages and rule[1] in pages:
                    idx0, idx1 = pages.index(rule[0]), pages.index(rule[1])
                    if idx0 > idx1:
                        changed = True
                        pages[idx0], pages[idx1] = pages[idx1], pages[idx0]
            if not changed:
                correct = True
    
    middle_sum = 0
    for i, pages in enumerate(books):
        if i not in correct_idx:
            middle_sum += pages[len(pages)//2]

    return middle_sum


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    rules, books = parse_input(data)

    # PART 1
    # test:    143
    # answer: 5762
    middle_sum_1, correct_idx = already_ordered(rules, books)
    print(middle_sum_1)

    # PART 2
    # test:    123
    # answer: 4130
    middle_sum_2 = order_pages(rules, books, correct_idx)
    print(middle_sum_2)