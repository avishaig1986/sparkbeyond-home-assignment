from collections import Counter
import glob


def most_common_words_from_txt_files_in_folder(folder_name):
    txtfiles = []
    try:
        for file in glob.glob(f"../{folder_name}/*.txt"):
            txtfiles.append(file)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

    for txtfile in txtfiles:
        try:
            with open(txtfile) as input_file:
            #build a counter from each word in the file
                count = Counter(word for line in input_file
                                for word in line.split())

            print(f"file:{txtfile}, most common word: {count.most_common()[0][0]}, repetitions: {count.most_common()[0][1]}")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
