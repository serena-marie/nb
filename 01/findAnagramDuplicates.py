# v2, optimized. Still feeling meh-y towards it. 
def findAnagramDuplicates(filename):
    with open(filename, 'r') as file:
        strings = file.read().split('\n')
        
        collection = {}
        for word in strings:
            # build frequency list for each string
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
                
            # Dict keys must be immutable, so convert to tuple
            key = tuple(freq)
            
            if collection.get(key) is None:
                collection[key] =  []
            collection[key].append(word)
            
        results = []
        for value in collection.values():
            if len(value) > 1:
                results.append(value[0])
        return results

""" v1: Runtime / space to be improved upon
def findAnagramDuplicates(filename):
    with open(filename, "r") as file:
        text = file.read()  # file is read in as one big chunk
        strings = text.split("\n")  # stored into a list

        collection = {}

        for originalString in strings:
            sortedString = "".join(sorted(originalString))

            if collection.get(sortedString) is None:  # doesn't exist in collection
                collection[sortedString] = {"original": originalString, "freq": 1}
            else:
                collection[sortedString]["freq"] = (
                    collection[sortedString].get("freq") + 1
                )

        results = []

        for key in collection:
            if collection[key]["freq"] > 1:
                results.append(collection[key]["original"])

    return results
"""

try:
    print(findDuplicates("nonsense.txt"))
except FileNotFoundError as e:
    print(f"Error! File not found. ==> {e}")
