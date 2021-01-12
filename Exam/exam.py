# ESC180 Final Examination, Fall 2020
#
# Aids allowed: the ESC180 website, a Python IDE. You must *not* use any other
# notes or internet website. You may must not communicate about the exam except
# to ask questions on Piazza.
#
# You may ask questions on the course Piazza. Please make your question private
# if it must disclose part of the solution. Otherwise, please make it public.
# Please check Piazza occasionally in case there are announcements or
# clarifications.
#
# You have 2.5 hours to work on the exam, and 30 minutes to submit it. You may
# keep writing the exam during the submission window, but it is your
# responsibility to make sure that the exam is submitted before the submission
# window closes. Late submissions will only be accepted from students who
# have been preapproved for a time extension through accessibility services.
#
# To be eligible to receive partial credit, you must submit a file which does
# not produce an error when read into Python. Any code that you know produces
# errors must be commented out. By themselves, comments/docstrings will not
# earn any points. However, they may help TAs in deciding how to award
# partial credit.
#
# Unless otherwise specified, you may import math and numpy, but not other
# modules.
#

################################################################################

#    Problem 1 (25 pts)
#
#    Up to 5 points will be awarded for making progress toward a correct
#    solution.
#
#    Assume you are given a list of filenames of text files. Assume
#    that the text files only contain the punctuation
#    [".", ",", "!", "?", "-"].
#    The files may also contain the newline character "\n".
#
#    For each file, there is a word that occurs in that file the most often --
#    the most frequent word. We want to find the word that is the most frequent
#    word in the most files.
#    Write a function that takes in a list of file names, and returns the word
#    that is the most frequent word in the most files. You can assume that there
#    are no ties: each file has one word that is the most frequent, and there
#    is one word that is the most frequent word in the most files.
#    For example, the function might be called as follows:
#
#    most_common_frequent_word(["diseases/" + filenames[0],
#                                "diseases/" + filenames[1],
#                                "diseases/" + filenames[2])
#    If the most frequent word in filesnames[0] is "a", the most frequent word in
#    filenames[1] is "the", and the most frequent word in filenames[2] is
#    "the", most_common_frequent_word should return "the"                               .
#    A non-word, such as "<a", would be considered a valid word for the files
#    given to you.
#
#    The words "Dog" and "dog" should be considered to be the same when computing
#    the frequency of words. The words "dogs" and "dog" should be considered
#    to be different.
#
#    You are encouraged to use helper functions.
#
#    For this problem, you may *not* import any Python modules.

def most_common(words):
    return max(set(words), key=lambda w: words.count(w))

def most_common_frequent_word(files):
    for i, name in enumerate(files):
        with open(name) as file:
            words = [word.lower() for line in file for word in line.split()]
        files[i] = most_common(words)

    return most_common(files)




################################################################################

#    Problem 2 (20 pts)
#
#    This problem will be auto-graded.
#
#
#    Recall that links in an html file are given in the format
#    <a href = "http://engsci.utoronto.ca">EngSci homepage</a>
#    Write a function that takes in the text of an html file, and returns a dictionary
#    whose keys are the link texts (e.g. "EngSci homepage") and whose values are
#    the corresponding URLs (e.g., "http://engsci.utoronto.ca"). You can assume
#    that link texts do not repeat.
#    Sample call:
#     get_links('<a href = "http://engsci.utoronto.ca">EngSci homepage</a>')
#    should return {"EngSci homepage": "http://engsci.utoronto.ca"}

def get_links(html_text):
    links = {}
    for i in range(len(html_text)):
        if html_text[i:i+11] == '<a href = "':
            end_of_link = html_text.find('">', i+11)
            links[html_text[end_of_link+2:html_text.find('</a>', end_of_link+2)]] = html_text[i+11:end_of_link]

    return links

###############################################################################

#   Problem 3 (10 pts)
#
#    Without using for-loops or while-loops, write  function for which
#    the tight asymptotic bound on the runtime complexity is O((n^2)*log(n)).
#    You may create helper functions, as long as they also do not use while-
#    and for-loops.
#    Justify your answer in a comment. The signature of the function must be

#Binary sort has O(log(n)) complexity
def binary_search(space, target):
    middle = len(space)//2
    if space[middle] == target:
        return middle
    elif space[middle] > target:
        return binary_search(space[:middle], target)
    else:
        return middle+binary_search(space[middle:], target)

#This function loops without using loops
def loop(i, space, n):
    binary_search(space, 0) #Call the log(n) complexity function
    if i > 0:
        loop(i-1, space, n)

#loop the log(n) function n^2 times
#O(n^2(log(n)))
def f(n):
    space = list(range(0, n))
    loop(n**2, space, n)


###############################################################################




###############################################################################
#  Problem 4 (15 pts)
#
#  This problem will be auto-graded.
#
#
#  It is possible to combine the numbers 1, 5, 6, 7 with arithemtic operations
#  to get 21 as follows: 6/(1-5/7).
#
#  Write a function that takes in a list of three numbers and a target number, and
#  returns a string that contains an expression that uses all the numbers
#  in the list once, and results in the target. Assume that the task is possible
#  without using parentheses.
#
#  For example, get_target_noparens([3, 1, 2], 7) can return "2*3+1" or "1+2*3"
#  (either output would be fine).

def product(l, r):
    pools = [tuple(l)]*r
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def permutations(l):
    if len(l) == 1:
        yield l

    for n in range(len(l)):
        for new in permutations(l[:n]+l[n+1:]):
            yield [l[n]]+new

def interleave(nums, operators):
    exp = ""
    for n, o in zip(nums, operators):
        exp += n+o

    return exp+nums[-1]

def get_target_noparens(nums, target):
    operators = list("*/+-")
    if len(nums) == 0:
        return str(nums[0])

    for combo in permutations(nums):
        combo = list(map(str, combo))
        for o in product(operators, len(nums)-1):
            expression = interleave(combo, o)

            try:
                result = eval(expression)
                if result == target:
                    return expression
            except:
                pass


#############################################################
#  Problem 5 (15 pts)
#
#  Up to 3 pts will be awarded for making progress toward a solution.
#
#  Now, write the function get_target which returns a string that contains an
#  expression that uses all the numbers in the list once, and results in the
#  target. The expression can contain parentheses. Assume that the task is
#  possible.
#  For example, get_target([1, 5, 6, 7], 21) can return "6/(1-5/7)"

def get_target(nums, target):
    operators = list("*/+-")
    if len(nums) == 0:
        return str(nums[0])

    for combo in permutations(nums):
        combo = list(map(str, combo))
        for n in range(0, len(nums)):
            for i in range(n+1, len(nums)):
                sub = list(combo)
                sub[n] = "("+sub[n]
                sub[i] = sub[i]+")"

                for j in range(0, len(nums)):
                    for k in range(j+1, len(nums)):
                        sub_sub = list(sub)
                        sub_sub[j] = "("+sub_sub[j]
                        sub_sub[k] = sub_sub[k]+")"
                        for o in product(operators, len(nums)-1):
                            expression = interleave(sub_sub, o)
                            try:
                                result = eval(expression)
                                if result == target:
                                    return expression
                            except:
                                pass

################################################################################