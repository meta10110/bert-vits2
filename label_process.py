import os

name = [
    ('carville', 'EN'),
    ('dugan', 'EN'),
    ('einstein', 'EN'),
    ('epsilon', 'EN'),
    ('eva', 'EN'),
]

out_file = f"filelists/red alert_out.txt"

def process():
    with open(out_file, 'w', encoding="utf-8") as wf:
        for item in name:
            ch_name = item[0]
            ch_language = item[1]
            path = f"./raw/{ch_name}"
            files = os.listdir(path)
            
            # 过滤出以ch_name开头的文件
            relevant_files = [f for f in files if f.startswith(f"{ch_name}_")]
            relevant_files.sort()  # 对文件进行排序

            for idx, f in enumerate(relevant_files, start=1):
                if f.endswith('.lab') or f.endswith('.txt'):
                    with open(os.path.join(path, f), 'r', encoding="utf-8") as perFile:
                        line = perFile.readline()
                        result = f"./dataset/{ch_name}/{f.split('.')[0]}.wav|{ch_name}|{ch_language}|{line}"
                        wf.write(f'{result}\n')

if __name__ == '__main__':
    process()
