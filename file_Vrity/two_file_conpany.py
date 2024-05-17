# 读取第一个文件的数据到集合file1_data
with open(r'G:\脚本验证文件\六安工厂_0428-测试-产品名称1_单码_0428-测试-001-批次5-2833_200.0W_20240428_P20240428141828378.txt', 'r') as file1:
    file1_data = set(line.strip() for line in file1)

# 读取第二个文件的数据到集合file2_data
with open(r'G:\脚本验证文件\六安工厂_0428-测试-产品名称1_单码_0428-测试-001-批次4-9311_200.0W_20240428_P20240428141828084.txt', 'r') as file2:
    file2_data = set(line.strip() for line in file2)

# 计算两个集合的交集
duplicates = file1_data.intersection(file2_data)

# 如果交集不为空，则输出重复的数据
if duplicates:
    print("存在重复数据")
    for duplicate in duplicates:
        print("重复的数据为：",duplicate)
else:
    print("没有发现重复数据。")