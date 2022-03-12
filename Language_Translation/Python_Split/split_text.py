import pandas as pd
import numpy as np


MAX_SAMPLES = 10000

def get_traslationCSV(language_name, file_name):
    with open("Term 7/40.319 - Statistical Machine Learning/1D/Language_Translation/Python_Split/{}.txt".format(file_name), encoding="utf8") as f:
        contents = f.readlines()
        # print(contents)
        english = []
        other_lang = []
        idx = 1
        for line in contents:
            # if idx > MAX_SAMPLES:
            #     break
            line = line.split('\t')
            english.append(line[0])
            other_lang.append(line[1])
            idx += 1
        # print(english[0:5])
        # print(other_lang[0:5])
        f.close()

    df = pd.DataFrame(list(zip(english, other_lang)),
                    columns= ["English", language_name])
    # print(df)
    df.to_excel('translation_{}.xlsx'.format(file_name),encoding='utf-16')



get_traslationCSV("Indonesian", "ind")