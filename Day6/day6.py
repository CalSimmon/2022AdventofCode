def part1(data):
    for x in range(len(data) - 3):
        curr = data[x:x + 4]
        if len(set(curr)) == len(curr):
            marker = x + 4
            break
    print(f"The first marker is after character {marker}.")
    
def part2(data):
    for x in range(len(data) - 13):
        curr = data[x:x + 14]
        if len(set(curr)) == len(curr):
            message = x + 14
            break
    print(f"The first message is after character {message}.")


if __name__ == "__main__":
    with open("day6input.txt", "r") as f:
        data = f.read()
    part1(data)
    part2(data)