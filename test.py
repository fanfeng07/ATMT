with open('baseline/prepared_data/dict.de','r') as f: #bpe/new_dict.de
    i = 0
    for line in f.readlines():
        if i <=15:
            word = line.rstrip().rsplit(' ',1)
            print(word)
        i+=1
        