import os
import pandas as pd
train_list = os.listdir('../dataset/csgo/images/train')
valid_list = os.listdir('../dataset/csgo/images/valid')
DATAPATH = 'dataset/csgo/images/'
total_train = []
total_valid = []
for i in range(len(train_list)):
    total_train.append(DATAPATH + 'train/' + train_list[i])


for i in range(len(valid_list)):
    total_valid.append(DATAPATH + 'valid/' + valid_list[i])

f = open("../dataset/csgo/train_list.txt", 'w+')
for i in range(len(train_list)):
    f.write(total_train[i])
    f.write('\n')

fs = open("../dataset/csgo/val_list.txt", 'w+')
for i in range(len(valid_list)):
    fs.write(total_valid[i])
    fs.write('\n')
