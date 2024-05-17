# with open(r"G:\test3.txt",'r') as file:
#     lines = file.readlines()
#
# lines = [line.strip() for line in lines]
#
# if len(lines) != len(set(lines)):
#     print("文件包含重复数据")
# else:
#     print("文件不包含重复数据")


def find_duplicates(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split()
    seen = set()
    duplicates = set()

    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)

    return duplicates

file_path = r'C:\Users\Administrator\Downloads\江苏_汤好喝-麻辣小龙虾-test_单码_测试007-批次2-6019_10.0W_20240403_P20240403113810192.txt'
duplicates = find_duplicates(file_path)
if len(duplicates) == 0:
    print("没有重复的数据")
else:
    print("重复的数据有：", duplicates)
    print("重复数据的条数为 :", len(duplicates))
