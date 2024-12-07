from src.tools.loader import load_data

TESTING = True


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    gone = False

    directions = {'v': (1,0), '^': (-1,0), '<' : (0,-1), '>': (0,1)}

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] in directions.keys():
                position = (i,j)
                fixed_position = (i,j)

    visited = [position]


    direction = directions[data[position[0]][position[1]]]
    fixed_direction = direction

    while not gone:
        new_position = (position[0]+direction[0], position[1]+direction[1])
        if new_position[0] not in range(len(data)) or new_position[1] not in range(len(data[0])):
            gone = True
        else:
            if data[new_position[0]][new_position[1]] in ['.', '<', '>', '^', 'v']:
                position = new_position
                visited.append(new_position)
            else:
                if direction == (1,0):
                    direction = (0,-1)
                elif direction == (-1,0):
                    direction = (0,1)
                elif direction == (0,-1):
                    direction = (-1,0)
                elif direction == (0,1):
                    direction = (1,0)

    print(len(set(visited)))


    loop_positions = []

    for i, visit in enumerate(visited):
        print(i)
        if visit != fixed_position:
            position = fixed_position
            direction = fixed_direction
            new_visits = [(position[0], position[1], direction)]
            done = False
            while not done:
                new_position = (position[0]+direction[0], position[1]+direction[1])
                if new_position[0] not in range(len(data)) or new_position[1] not in range(len(data[0])):
                    done = True
                else:
                    if data[new_position[0]][new_position[1]] in ['.', '<', '>', '^', 'v'] and new_position != visit:
                        position = new_position
                    else:
                        if direction == (1,0):
                            direction = (0,-1)
                        elif direction == (-1,0):
                            direction = (0,1)
                        elif direction == (0,-1):
                            direction = (-1,0)
                        elif direction == (0,1):
                            direction = (1,0)

                if (new_position[0], new_position[1], direction) in new_visits:
                    loop_positions.append(visit)
                    done = True
                new_visits.append((new_position[0], new_position[1], direction))

    print(len(set(loop_positions)))