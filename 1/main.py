if __name__ == "__main__":
    with open('input.txt', 'r') as puzzle_input:
        lines = [int(line) for line in puzzle_input.read().splitlines()]
        print(len([index for index in range(1,len(lines)) if index > 0 and lines[index] > lines[index-1]]))
