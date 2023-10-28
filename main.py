# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 获取txt文本行数
# [in] file_path: TXT文件路径
def get_txt_line(file_path):
    # 打开文件，把文件句柄给到“file”
    with open(file_path, 'r') as file:
        # 将一行列为一个数组
        lines = file.readlines()
        # 计算有多少行
        line_count = len(lines)
    return line_count

# 去掉"\n"
# [in] word_list: 单词表
def remove_wrap(word_list):
    # 逐行去掉\n
    for i in range(len(word_list)):
        # 去除"\n"后，重新赋值回去
        word_list[i] = word_list[i].replace('\n', '')

# 保存为新的txt
# [in] new_path_file: 要保存的文件路径
# [in] new_word_list: 要保存的单词表
def word_save(new_path_file, new_word_list):
    # 创建新的TXT文件，并设置为写操作
    new_file_path = open(new_path_file, "w")
    # 循环写入单词
    for line in new_word_list:
        # 每个单词后面加个换行
        new_file_path.write(line + "\n")
    # 完成写操作后，关闭该文件
    new_file_path.close()
    print("保存完成！新文件名:", new_path_file)

# 单词排列
# [in] file_path: 要排序的TXT文件路径
def word_sort(file_path):
    with open(file_path, 'r') as file:
        # 获取每一行的数据
        word_list = file.readlines()
        # 去掉"\n"
        remove_wrap(word_list)
        # 按照单词长度排序
        new_list = sorted(word_list, key=lambda i:len(i), reverse=False)
    return new_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # 存储文件位置
    main_file_path = "line_test.txt"
    main_new_file_path = "new_word.txt"
    # 获取单词数量
    word_line = get_txt_line(main_file_path)
    print("总共有%d个单词" %(word_line))
    # 单词排序
    new_list = word_sort(main_file_path)
    # 将排序后的单词保存成新的TXT
    word_save(main_new_file_path, new_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
