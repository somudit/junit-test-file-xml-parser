from os import listdir
import xml.etree.ElementTree as ET


PATH = '/home/mudit/junit-test-file-xml-parser/test_files'

def get_failed_test_files():
    file_list = listdir(PATH)
    valid_files = []
    for file in file_list:
        if '.xml' in file:
            valid_files.append(file)
    for test_file in valid_files:
        tree = ET.parse(PATH+test_file)
        root = tree.getroot()
        if root.tag == 'testsuite':
            str = "{file_name} :- \n No. of test = {tests} \n Failed = {failures} \n " \
                  "time taken : {time}".format(file_name=test_file, tests=root.attrib['tests'],
                                               failures=root.attrib['failures'], time=root.attrib['time'])
        for test_case in root.findall('testcase'):
            for child in test_case:
                if child.tag == 'failure':
                    str += test_case.get('name'))

get_failed_test_files()
