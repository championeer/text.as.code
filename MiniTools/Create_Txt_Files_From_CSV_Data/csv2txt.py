"""
作者：XYU
版本：1.0

说明：
这个脚本用于将CSV文件中的数据转换为单独的文本文件。
它读取CSV文件中的'title'和'text'列，
并为每一行创建一个以标题命名的txt文件，
文件内容为对应的文本。

使用方法:
1. 运行脚本
2. 在提示时输入CSV文件的路径
3. 脚本将在当前目录下创建txt文件

注意:
- CSV文件应包含'title'和'text'列
- 文件名会被清理，只保留字母、数字、空格、下划线和连字符
- 如果遇到任何错误，脚本将打印错误信息
"""

import csv
import os

# 增加字段大小限制
import sys
csv.field_size_limit(sys.maxsize)  # 将字段大小限制设置为系统允许的最大值

def csv_to_txt(csv_file):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                title = row['title']
                text = row['text']
                
                filename = ''.join(c for c in title if c.isalnum() or c in (' ', '_', '-'))
                filename = f"{filename}.txt"
                
                with open(filename, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text)
                
                print(f"已创建文件: {filename}")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    csv_file = input("请输入CSV文件路径: ")
    if os.path.exists(csv_file):
        csv_to_txt(csv_file)
    else:
        print("文件不存在，请检查路径是否正确。")
