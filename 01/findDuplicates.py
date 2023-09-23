# v2, runtime and space to be improved upon
def findDuplicates(filename):
    with open(filename, "r") as file:
        text = file.read()  # file is read in as one big chunk
        strings = text.split("\n")  # stored into a list

        collection = {}

        for originalString in strings:
            sortedString = "".join(sorted(originalString))

            existence = collection.get(sortedString)

            if (
                existence is None
            ):  # doesn't exist in collection, might be able to skip variable creation but test it works first
                collection[sortedString] = {"original": originalString, "freq": 1}
            else:
                collection[sortedString]["freq"] = (
                    collection[sortedString].get("freq") + 1
                )

        results = []

        for key in collection:
            if collection[key]["freq"] > 1:
                results.append(collection[key]["original"])
        """ runtime error: dictionary changed size during iteration
        for key in collection:
            if collection[key]['freq'] == 1:
                del collection[key]
        """

    return results


try:
    print(findDuplicates("nonsense.txt"))
except FileNotFoundError as e:
    print(f"Error! File not found. ==> {e}")
