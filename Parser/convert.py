import os
import pandas as pd
from Parser.TableParcer import TableParcer


def parce_folder_xls(source_directory, result_directory):
    if not os.path.exists(result_directory):
        os.mkdir(result_directory)
    for directory in os.listdir(source_directory):
        if not os.path.exists(result_directory + f'/{directory}'):
            os.mkdir(result_directory + f'/{directory}')
        for file in os.listdir(f'{source_directory}/{directory}'):
            if file.endswith('.xls'):
                TableParcer.get_(f'{source_directory}/{directory}/{file}',
                                     dest_file_name=f'{result_directory}/{directory}/{file}x')


if __name__ == '__main__':
    convert_files_to_xlsx('Datasets', 'additionalData/datasets_xlsx')
