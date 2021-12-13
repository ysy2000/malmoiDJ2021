import pandas as pd
import csv

def sort_target(x):
        return x[1]

def tocken_freq(sentence_list, file_names):
    char_count = {}

    for k, sentence in enumerate(sentence_list):
        #print(sentence)
        try:
            for char in sentence:
                try:
                    char_count[char] += 1
                except:
                    char_count[char] = 1
        except:
            # 안되는 애들 모아두기
            with open("/home/jyseo/Hackathon2021/aihub/out.txt", "a") as f:
                f.write(file_names[k]+'\n')

    char_count = dict(sorted(char_count.items(), key=sort_target, reverse=True))

    return char_count


if __name__ == '__main__':

    labels = []
    file_names = []
    Data_list1 = pd.read_csv("/home/jyseo/Hackathon2021/aihub/aihub_list_dev_new.csv")
    Data_list2 = pd.read_csv("/home/jyseo/Hackathon2021/aihub/aihub_list_train_new.csv")
    Data_list3 = pd.read_csv("/home/jyseo/Hackathon2021/data/data_list_dev_new_11.csv")
    Data_list4 = pd.read_csv("/home/jyseo/Hackathon2021/data/data_list_train_new_12.csv")

    Data_lists = [Data_list1,Data_list2,Data_list3,Data_list4]
    for Data_list in Data_lists:
        #print(Data_list)
        for i in range(len(Data_list)):
            labels.append(Data_list.iloc[i].text)
            file_names.append(Data_list.iloc[i].file_name)
    #print(len(train_labels))
    csvPATH = "/home/jyseo/Hackathon2021/AIHack2021_CC/labels_for_chars_all.csv"        
    # script 와 file csv에 쓰기
    with open(csvPATH, 'a', newline='') as f:
        wr = csv.writer(f)
        char_freq = tocken_freq(labels,file_names)
        for i, char in enumerate(list(char_freq.keys())):
            wr.writerow([i, char, char_freq[char]]) 
