# function that removes punctuation characters
def strip_punctuation(str):
    for char in punctuation_chars:
        if char in str:
            str = str.replace(char, "")
    return str


# function that calculates how many words in a string are considered positive words
def get_pos(str):
    positive_words_count = 0
    str = strip_punctuation(str)
    words_list = str.split()
    for word in words_list:
        word = word.lower()
        if word in positive_words:
            positive_words_count +=1
    return positive_words_count


# function that calculates how many words in a string are considered negative words
def get_neg(str):
    negative_words_count = 0
    str = strip_punctuation(str)
    words_list = str.split()
    for word in words_list:
        word = word.lower()
        if word in negative_words:
            negative_words_count +=1
    return negative_words_count

# I added '-' and '…' (the ellipsis symbol, not just three dots one after another) 
# to punctuation_chars, since those symbols are also in the text
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '-', '…']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_w:
    for lin in pos_w:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as neg_w:
    for lin in neg_w:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


tweets = []

# open the csv
fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()
# split the first row to get the field names
header = lines[0]
# split other rows to get values
field_names = header.strip().split(',')
for row in lines[1:]:
    vals = row.strip().split(',')
    # transform text to int for number of retweets and replies
    vals[1] = int(vals[1])
    vals[2] = int(vals[2])
    tweets.append(vals)


# create output file
outfile = open("resulting_data.csv", "w")
# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score') 
outfile.write('\n')

# output each of the rows:
for i in tweets:
    pos_wrd = get_pos(i[0])
    neg_wrd = get_neg(i[0])
    net_wrd = pos_wrd - neg_wrd
    row_string = '{},{},{},{},{}'.format(i[1], i[2], pos_wrd, neg_wrd, net_wrd)
    outfile.write(row_string)
    outfile.write('\n')
print(outfile)
outfile.close()
