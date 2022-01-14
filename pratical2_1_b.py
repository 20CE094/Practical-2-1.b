#Name-Nehal Patel
#ID- 20CE094
#Github link: https://github.com/20CE094/Practical-2-1.b.git
dict = {1:'110', 2:'69', 3:'9'}
e = {4:'z', 5:'y', 6:'x'}
#user-defined function to merge two dictionaries
def merge(dict,e):
    return (e.update(dict))
#printing updated dictionary
print(merge(dict,e))
print (e)   