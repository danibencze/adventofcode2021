if __name__ == "__main__":
    with open('input.txt', 'r') as puzzle_input:
        lines = [line.split(" ") for line in puzzle_input.read().splitlines()]
        counter = {"forward": 0, "down": 0, "up": 0}
        for action in lines:
            print(action)
            counter[action[0]] += int(action[1])
        print((counter["down"]-counter["up"]) * counter["forward"])
