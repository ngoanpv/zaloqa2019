# 1st place solution for Zalo AI 2019 - Vietnamese Wiki Question Answering

## Overview 
Given a question, related paragraphs from a Wikipedia article (in the shuffle order), the task is finding paragraph which answers the question of each test case.

F1 measure based on precision and recall is used to rank competing submissions. 

For detailed, visit: https://challenge.zalo.ai/portal/question-answering

## About Data?

- train data: 18108 question text pairs
- test data: 2678 question text pairs

Some interesting/confusing/mistake question text pairs:

| Question                                         | Text                                                                                                                                                    | Title                                         | Label |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|-------|
| Việt nam ra nhập liên hợp quốc năm bao nhiêu     | Quốc gia Việt Nam và Việt Nam Dân Chủ Cộng Hoà cùng nộp đơn vào tháng 10 năm 1949 .                                                                     | Quá trình gia nhập Liên Hợp Quốc của Việt Nam |  ?    |
| Ngọn núi cao nhất thế giới tính từ mực nước biển | Độ cao so với mực nước biển của mặt đất thay đổi từ -418 m ở biển Chết tới 8.848 m trên đỉnh Everest và độ cao trung bình trên mặt nước biển là 840 m . | Trái Đất                                      | ?     |
| Lý Thái Tổ trị vì bao nhiêu năm?                 | Lý Thái Tổ ( ) , là vị hoàng đế sáng lập nhà Lý trong lịch sử Việt Nam , trị vì từ năm 1009 đến khi qua đời vào năm 1028 .                              | Lý Thái Tổ                                    | ?     |

## Approaches 

We used handcrafted features, bert and combined on original data (only use question, text), or add title data, add transitivity rules and add external data (Squad 2.0 translated to Vietnamese).

We have made 73 single models from the above combinations. 
## Final Solution 
We selected the best model to submit. Although ensemble version have the better result, however the predict time is so much longer than one model, so one model is submit. The config is below:

Init checkpoint at https://github.com/lampts/bert4vn (BERT for Vietnamese)

num_train_epochs = 5.0

max_seq_length = 512 

train_batch_size = 128

learning_rate = 2e-5


## Train 
Please download the init checkpoint at [here]() and put into the folder checkpoint.

Put data in the folder /data/

Run command ``` sh train.sh ```


## Predict
If you want to only predict, please download the checkpoint of trained model at [here]()

Run command: ``` sh predict.sh ```. 

## What's next?

ALBERT for Vietnamese will be release at https://github.com/ngoanpv/albert_vi 

