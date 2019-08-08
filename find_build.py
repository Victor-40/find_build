import json
import os
import re
import sys
import PySimpleGUI as sg


root_path = r'\\rum\dfs\new_versions'
sg.ChangeLookAndFeel('LightGreen')

with open('cfg/dir_list.json') as fi:
    prod_dct = json.load(fi)

search_dirs = [os.path.join(root_path, item) for item in prod_dct['prod_dirs']]

all_list = list()
for _dir in search_dirs:
    root_obj = os.scandir(_dir)
    for item in root_obj:
        all_list.append(item.path)

reference_build = sg.PopupGetFolder('Choose reference build', initial_folder=root_path, size=(80, 1))
if not reference_build:
    sys.exit(0)

patt = re.compile(r'-(\d\d\d\d)(__|_x64__)(.*$)')
m = re.search(patt, reference_build)
if m:
    build = m.group(1)
    tag = m.group(3)
else:
    print('ERROR: no matches')
    sys.exit(0)

patt = re.compile(r'-%s(__|_x64__)%s' % (build, tag), re.I)

fin_lst = list()
for item in all_list:
    m = re.search(patt, item)
    if m:
        fin_lst.append(item)

for i in sorted(fin_lst):
    print(i)



