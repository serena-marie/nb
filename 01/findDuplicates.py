# I should only be adding to the collection if it IS a duplicate
# If it's the first occurence, need to keep track, if it's the second occurence need to add to list
def findDuplicates(filename):
  with open(filename, 'r') as file:
    text= file.read() # file is read in as one big chunk
    strings = text.split('\n') # stored into a list
    
    collection = {}
    
    for originalString in strings:
      sortedString = ''.join(sorted(originalString))
      existence = collection.get(sortedString)
      
      if existence is None: # doesn't exist in collection, might be able to skip variable creation but test it works first
          collection[sortedString] = originalString
      """
      if collection[sortedString]: # this wont work because you'll get a key error
          continue
      else
      """            
  return collection.items()
        
        

try:
    print(findDuplicates('mininonsense.txt'))
except FileNotFoundError as e:
    print(f'Error! File not found. ==> {e}')
