import os

import labelimg_xml

path_dir = os.getcwd()
original_dir = path_dir + '/original/'
result_dir = path_dir + '/result/'

file_list = [_ for _ in os.listdir(original_dir) if _.endswith('.xml')]

for file in file_list:
    title, table = labelimg_xml.read_xml(original_dir, file)

    for cell in table:
        if cell[0].find('P') > -1:
            cell[0] = 'Platelet'

    labelimg_xml.write_xml(title, table, result_dir, file)