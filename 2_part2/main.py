if __name__ == "__main__":
    with open('input.txt', 'r') as puzzle_input:
        lines = [line.split(" ") for line in puzzle_input.read().splitlines()]
        stats = {"horizontal": 0, "depth": 0, "aim": 0}
        for action in lines:
            action[1] = int(action[1])
            if action[0] == "forward":
                stats["horizontal"] += action[1]
                stats["depth"] += action[1]*stats["aim"]
            elif action[0] == "down":
                stats["aim"] += action[1]
            elif action[0] == "up":
                stats["aim"] -= action[1]
        print(stats)
        print(stats["horizontal"] * stats["depth"])
