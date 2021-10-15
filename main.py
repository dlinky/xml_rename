import os

import labelimg_xml

path_dir = os.getcwd()
original_dir = path_dir + '/original/'
result_dir = path_dir + '/result/'

for (path, dir, files) in os.walk('C:/Users/user/Desktop/혈구도말 레이블/데이터구축(2021.07.27)/'):
    for filename in files:
        if str(filename).endswith('.xml'):
            print('processing %s : '%str(filename), end='')
            title, table = labelimg_xml.read_xml(path+"/", filename)
            count = 0
            for cell in table:
                if cell[0].find('P') > -1:
                    cell[0] = 'Platelets'
                if cell[0].find('p') > -1:
                    cell[0] = 'Platelets'
            labelimg_xml.write_xml(title, table, path+"/", filename)