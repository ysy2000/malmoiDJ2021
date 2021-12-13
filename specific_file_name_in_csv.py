import pandas as pd
import csv

def sort_target(x): # 1번째 data
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
### data 불러오기
    labels = []
    file_names = []
    csvPATH = "/home/ysy/AIHack2021_CC/specific_file_name.csv"  
    Data_list1 = pd.read_csv("/home/ysy/2021AI_data_Hackarthon/data_list_dev.csv")
    Data_list2 = pd.read_csv("/home/ysy/2021AI_data_Hackarthon/data_list_train.csv")

    # print(type(Data_list))
    data2num = {"Data_list1" : 1 , "Data_list2" : 2}
    num2Add = ["/home/ysy/dataset_malmoiDJ2021/dev/", "/home/ysy/dataset_malmoiDJ2021/train/"]

    Data_lists = [Data_list1,Data_list2]
    # print(type(Data_lists))
    # print(Data_list)
    for Data_list in Data_lists:
        # print(Data_list)
        for i in range(len(Data_list)):
            labels.append(Data_list.iloc[i].text)
            file_names.append(num2Add[data2num[Data_list]]+Data_list.iloc[i].file_name)
    # print(len(train_labels))
          
    # script 와 file csv에 쓰기
    with open(csvPATH, 'a', newline='') as f:
        wr = csv.writer(f)
        char_freq = tocken_freq(labels,file_names)
        for i, char in enumerate(list(char_freq.keys())):
            wr.writerow([i, char, char_freq[char]]) 
