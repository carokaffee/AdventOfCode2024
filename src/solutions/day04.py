from src.tools.loader import load_data

TESTING = False


#def parse_input(data):
#    for line in data:



if __name__ == "__main__":
    puzzle = load_data(TESTING, "\n")

    big_puzzle = ['' for _ in range(len(puzzle)+8)]
    for i in range(4):
        big_puzzle[i] = '.' * (len(puzzle[0])+8)
        big_puzzle[-i-1] = '.' * (len(puzzle[0])+8)

    for i,line in enumerate(puzzle):
        big_puzzle[i+4] += '....' + line + '....'

    xmas_count = 0

    for i in range(4, len(big_puzzle)-3):
        for j in range(4, len(big_puzzle[0])-3):
            rightdown = ''
            rightup = ''
            leftdown = ''
            leftup = ''
            left = ''
            right = ''
            up = ''
            down = ''
            for x in range(4):
                rightdown += big_puzzle[i+x][j+x]
                leftup += big_puzzle[i-x][j-x]
                rightup += big_puzzle[i-x][j+x]
                leftdown += big_puzzle[i+x][j-x]
                left += big_puzzle[i][j-x]
                right += big_puzzle[i][j+x]
                up += big_puzzle[i-x][j]
                down += big_puzzle[i+x][j]
            xmas_count += (rightdown == 'XMAS')
            xmas_count += (rightup == 'XMAS')
            xmas_count += (leftdown == 'XMAS')
            xmas_count += (leftup == 'XMAS')
            xmas_count += (left == 'XMAS')
            xmas_count += (right == 'XMAS')
            xmas_count += (up == 'XMAS')
            xmas_count += (down == 'XMAS')

    print(xmas_count)

    rightdown_coords = set()
    rightup_coords = set()

    for i in range(4, len(big_puzzle)-3):
        for j in range(4, len(big_puzzle[0])-3):
            rightdown = ''
            rightup = ''
            leftdown = ''
            leftup = ''
            for x in range(3):
                rightdown += big_puzzle[i+x][j+x]
                leftup += big_puzzle[i-x][j-x]
                rightup += big_puzzle[i-x][j+x]
                leftdown += big_puzzle[i+x][j-x]
            if rightdown == 'MAS':
                rightdown_coords.add((i+1,j+1))
            if leftup == 'MAS':
                rightdown_coords.add((i-1,j-1))
            if rightup == 'MAS':
                rightup_coords.add((i-1,j+1))
            if leftdown == 'MAS':
                rightup_coords.add((i+1,j-1))

    print(len(rightdown_coords.intersection(rightup_coords)))