import os

name = [
    ('character_zh_6', 'ZH'),
]

out_file = f"filelists/character_zh_6.list"

def process():
    with open(out_file, 'w', encoding="utf-8") as wf:
        for item in name:
            ch_name = item[0]
            ch_language = item[1]
            path = f"./raw/{ch_name}"
            files = os.listdir(path)
            for f in files:
                if f.endswith('.lab') or f.endswith('.txt'):
                    with open(os.path.join(path, f), 'r', encoding="utf-8") as perFile:
                        line = perFile.readline().strip()  # 使用strip去除末尾空白字符
                        result = f"./dataset/{ch_name}/{f.split('.')[0]}.wav|{ch_name}|{ch_language}|{line}"
                        wf.write(f'{result}\n')

if __name__ == '__main__':
    process()
