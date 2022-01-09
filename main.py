# Program to generate permutations of groups of data
import pprint


GROUPS = {
    "top": 3,
    "jungle": 5,
    "mid": 3,
    "bot": 1,
    "support": 5,
}

# Use names to provide a list of names, otherwise will default to 'group-n'
NAMES = {
    "top": ["asdf", "qwer", "zxcv"],
}


def main():
    data = {}
    matches = {}

    def findLargest(data):
        largest = ""
        for group in data:
            if largest == "" or len(data[group]) > len(data[largest]):
                largest = group

        return largest

    def getSet(group, index):
        size = len(group)

        if size < 2:
            return group[0]

        while index >= size:
            index -= size

        return group[index]

    def generateGroup(group, number):

        try:
            return [f"{NAMES[group][i]}" for i in range(number)]
        except:
            return [f"{group}-{i + 1}" for i in range(number)]

        # if len(NAMES) > 0:
        #     return [f"{group}-{i + 1}" for i in range(number)]
        # else:
        #     return [f"{group}-{i + 1}" for i in range(number)]

    def generateBlocks(data):
        block = {}
        for group in data:
            row = data[group]
            temp_block = {}
            if len(row) == 1:
                member = row.pop()
                temp_block[0] = [member, f"{group}-*"]
            else:
                for i in range(len(row)):
                    member = row.pop()
                    for opponent in row:
                        temp_block[len(temp_block)] = [member, opponent]

            block[group] = temp_block

        return block

    def formatPrint(dataset, indent=4):
        tab = "".join([" " for _ in range(indent)])

        for group in dataset:
            team1 = dataset[group][0]
            team2 = dataset[group][1]
            print(f"{tab}{group.upper()}: {team1} | {team2}")

    # Create data
    for group in GROUPS:
        data[group] = generateGroup(group, GROUPS[group])

    block = generateBlocks(data)
    largest = findLargest(block)
    size = len(block[largest])

    print(f"First largest group is {largest} at size {size}")

    # Print matches
    for i in range(size):
        subset = {}
        for group in GROUPS:
            subset[group] = getSet(block[group], i)
        matches[i] = subset
        print(f"Match - {i + 1}")
        formatPrint(subset)

    return


main()
