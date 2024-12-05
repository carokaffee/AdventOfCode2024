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


def correctly_ordered_idx(rules, books):
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
    return correct_idx


def order_pages(rules, books):
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
    return books


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    rules, books = parse_input(data)

    correct_sum = 0
    correct_idx = correctly_ordered_idx(rules, books)

    for idx in correct_idx:
        corr_ord = books[idx]
        correct_sum += corr_ord[len(corr_ord)//2]

    print(correct_sum)


    
    ordered_pages = order_pages(rules, books)
    new_ordering_sum = 0

    for i, pages in enumerate(books):
        if i not in correct_idx:
            new_ordering_sum += pages[len(pages)//2]

    print(new_ordering_sum)