'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    # we can only evaluate if there are at least 2 letters in the word
    if len(word) >= 2:
        # if the first letter is 't' and the second is 'h' increment count by 1
        if word[:2] == 'th':
            count += 1
            return count + count_th(word[2:]) # because you know the "second" letter can't be a t
        else:
            return count_th(word[1:])
    
    else:
        return count
   
    
    
# test1 = 'thethethe'
# test2 = 'a'
# test3 = 'theendoftheworld'

# testing = [test1, test2, test3]

# for each in testing:
#     print(count_th(each))