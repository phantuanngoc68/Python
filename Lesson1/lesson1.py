#Read file
def count_word(list_word):
  return len(list(dict.fromkeys(list_word)))
try:
    #path = input("Enter file Name? ")
    path = 'lesson1.txt';
    dem = 0
    with open(path, 'r') as f:
        f_contents = f.read().split()
        print("Count the unique word from a text file = {0}".format(count_word(f_contents)))
except:
    print("Error")




