#!/bin/sh

# ../data にJAQKETのクイズデータが存在しないならcurlで取得する

FILE="./data/jaqket_train.json"

if [ ! -e $FILE ]; then
    curl "https://jaqket.s3-ap-northeast-1.amazonaws.com/data/train_questions.json" --output $FILE
else
    echo "jaqketのクイズデータは存在しています。"
fi