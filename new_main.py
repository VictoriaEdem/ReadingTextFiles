import string


def read_file_content(filename):
    f = open('story.txt', 'r')
    text_file = f.read()
    f.close()
    return text_file
result = read_file_content('story.txt')
#print(result)



def count_words():
    text = read_file_content("./story.txt")
    s_text = text.translate(str.maketrans("", "", string.punctuation))
    #print(s_text)
    split_stripped_text = s_text.split()
    #print(split_stripped_text)
    count ={}
    for i in split_stripped_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
    
print(count_words())


