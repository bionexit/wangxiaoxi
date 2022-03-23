import csv
import os


class dic_csv_typewriter:
    def __init__(self, csv_filename, csv_path, write_type='w', encoding='utf-8'):
        """___init___ _summary_

        Initialize the csv file

        Args:
            filename (str): specify the csv file name, NO EXTENSION .csv needed
            writetype (str): [w,a], w mode is default when init
            encoding (str, optional): _description_. Defaults to 'utf-8'.
        """

        self.csv_path = csv_path
        self.csv_filename = os.path.join(self.csv_path, csv_filename+'.csv')
        self.write_type = write_type
        self.encoding = encoding

        self.csvFile = open(self.csv_filename,
                            self.write_type, encoding=self.encoding)

    def write_headline(self, input_dict):
        """headline _summary_

        input any dict for the headline

        Args:
            dic (_type_): _description_
        """
        
        head_line = []
        for headers in input_dict.keys():  # 把字典的键取出来,注意不要使用sorted不然会导致键的顺序改变
            head_line.append(headers)

        self.dict_writer = csv.DictWriter(self.csvFile, head_line)
        self.dict_writer.writeheader()
        # f = open(self.csv_file,'a',encoding=self.encoding)
        # writer = csv.DictWriter(f, fieldnames=self.head_line)
        # writer.writeheader()
        # f.close()

    def write_content(self, input_dict):
        self.dict_writer.writerow(input_dict)

    def close(self):
        self.csvFile.close()


csv_path = os.path.abspath(os.path.dirname(__file__))
csvfile = dic_csv_typewriter('234', csv_path)
dict = {'234': 9999, 'asdf': 9999, 'asf': 9999}
dict1 = {'234': 99991, 'asdf': 99199, 'asf': 99199}
csvfile.write_headline(dict)
csvfile.write_content(dict1)
csvfile.write_content(dict1)
csvfile.close()
