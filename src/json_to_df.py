import pandas as pd
import re
from mecab_parse import MecabParser
from cabocha_parse import CabochaParser
import access_DB
from util import *

def get_quetion_data():
    data = []
    pattern = re.compile('"(question)": "(.+?)", "(answer_entity)": "(.+?)",')
    with open("./data/jaqket_train.json",mode="r") as r_file:
        lines = r_file.readlines()
        for line in lines:
            resulet = re.findall(pattern,line)[0]
            data_dic = {resulet[0]:resulet[1],resulet[2]:resulet[3]}
            data.append(data_dic)
    jaqket_df = pd.DataFrame(data)
    return jaqket_df

def main():
    file_path = "./result_data/keywords.csv"
    qa_df = get_quetion_data()
    sample_q_text = qa_df.head(10)["question"]
    mecab = MecabParser()
    cabocha = CabochaParser()
    keywords_list = []
    chunks_list = []
    for q_text in sample_q_text:
        print("Q: " + q_text)
        keywords = mecab.make_keywords(q_text)
        chunks = cabocha.make_chunks(q_text)
        keywords_list.append(keywords)
    write_value(file_path, keywords_list)
    return keywords_list



if __name__ == "__main__":
    main()