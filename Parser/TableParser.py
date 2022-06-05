import pandas as pd
import os


class TableParser:
    @staticmethod
    def get_parsed_df(xls_file):
        parse_column = [
            'date', 'number', 'patient', 'age', 'called by',
            'address',
            'Occasion', 'Call Type', 'Sick Type',
            'Diagnose', 'Result',
            'Delivered to', 'brigade', 'substation',
            'Accepted time', 'Arrived time', 'hospitalized', 'executive'
        ]

        parse_form = [
            [0, 3, 6, 16, 19],
            [1],
            [1, 11, 18],
            [1, 11],
            [1, 8, 17],
            [8, 11, 14, 20]
        ]

        df = pd.read_excel(xls_file)
        df.columns = [i for i in range(len(df.columns))]

        df_rows = df.iterrows()
        parsed_data = []
        while True:
            try:
                parsed_row = []
                for form_row in parse_form:
                    cur_row = next(df_rows)[1]
                    while pd.isna(cur_row[2]) and len(parsed_row) == 0:
                        cur_row = next(df_rows)[1]
                    for form_col in form_row:
                        parsed_row.append(cur_row[form_col])
                parsed_data += [parsed_row]
            except StopIteration:
                break
        return pd.DataFrame(parsed_data, columns=parse_column)

    @staticmethod
    def create_folder_xlsx(source_directory, result_directory):
        if not os.path.exists(result_directory):
            os.mkdir(result_directory)
        for directory in os.listdir(source_directory):
            if not os.path.exists(result_directory + f'/{directory}'):
                os.mkdir(result_directory + f'/{directory}')
            for file in os.listdir(f'{source_directory}/{directory}'):
                if file.endswith('.xls'):
                    df = TableParser.get_parsed_df(f'{source_directory}/{directory}/{file}')
                    df.to_excel(f'{result_directory}/{directory}/{file}x')


if __name__ == '__main__':
    filepath = '../Datasets/data_xls/calls_2020/Журнал активных вызовов 01-2020.xls'
    # df = TableParser.get_parsed_df(filepath)
    # TableParser.create_folder_xlsx('../Datasets/data_xls', '../Datasets/processed_xlsx')



