import json
import os


def read_file(file_name):
    # 文件存储位置
    store_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "conf" + os.sep \
                 + file_name+".txt"
    file = open(store_path, "r", encoding='utf-8')
    temp = file.read()
    file.close()
    user_info = dict()
    # 如果文件内容不为空，则直接获取到json，进而转换成dict
    if temp != "":
        user_info = json.loads(temp)
    return user_info


def write_file(file_name, dicts):
    store_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "conf" + os.sep \
                 + file_name + ".txt"
    # 文件打开格式也需要utf-8编码
    file = open(store_path, "w", encoding='utf-8')
    # unicode转string
    file.write(json.dumps(dicts).encode("utf-8").decode("unicode_escape"))
    file.close()


def test():
    print("test")

