import os


root_path = r'D:\!Reports\4534-2019'


length_paths = set()

# root_obj = os.scandir(root_path)
# for item in root_obj:
#     print(item.name)


for root, dirs, files in os.walk(root_path):
    for file in files:
        pp = os.sep.join([root, file])
        print(pp)
        print(len(pp))
        length_paths.add(len(pp))


print('max_lenght=', sorted(length_paths)[-1])

q = r'\\rum-cherezov-dt'
z = '4534__git--efd_2019_1.4534_26.02.2019_1'
print('q=', len(q))
print('z=', len(z))