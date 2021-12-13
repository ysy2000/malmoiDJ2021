import pandas as pd
import csv

# def sort_target(x): # 1번째 data
#         return x[1]

if __name__ == '__main__':
### data 불러오기
    labels = []
    file_names = []
    csvPATH = "/home/ysy/AIHack2021_CC/specific_file_name.csv"  
    Data_list1 = pd.read_csv("/home/ysy/2021AI_data_Hackarthon/data_list_dev.csv")
    # print(type(Data_list1))  =  <class 'pandas.core.frame.DataFrame'>
    Data_list2 = pd.read_csv("/home/ysy/2021AI_data_Hackarthon/data_list_train.csv")

    
    data2num = {"Data_list1" : 1 , "Data_list2" : 2}
    num2Add = ["/home/ysy/dataset_malmoiDJ2021/dev/", "/home/ysy/dataset_malmoiDJ2021/train/"]
    # print(type(data2num))  =  <class 'dict'>
    # print(type(num2Add))  =  <class 'list'>

    Data_lists = [Data_list1,Data_list2]
    # print(str(Data_lists[0]))
    # print(type(Data_lists))  =  <class 'list'>
#     # print(Data_list1) =  
#                                                  file_name                             text
# 0      1752/K00021752-AFG13-L1N2D1-E-K0KK-00546684.wav                        큰 소리로 말해요

    for Data_list in Data_lists:
        # print(Data_list)
        for i in range(len(Data_list)):
            labels.append(Data_list.iloc[i].text)
            file_names.append(num2Add[1]+Data_list.iloc[i].file_name)
    # print(len(train_labels))
          
    # script 와 file csv에 쓰기
    with open(csvPATH, 'a') as f:
        wr = csv.writer(f)
        for Data_list in Data_lists:
            for i in range(len(Data_list)):
                wr.writerow([file_names[i],labels[i]])
        # char_freq = tocken_freq(labels,file_names)
        # for i, char in enumerate(list(char_freq.keys())):
        #     wr.writerow([i, char, char_freq[char]]) 
