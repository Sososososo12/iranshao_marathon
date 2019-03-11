import os

pid=0
url=''
def create_article_to_txt(pid,url):
    """
    创建txt，并且写入
    """
    path_file_name = './action_{}.txt'.format(pid)
    if not os.path.exists(path_file_name):
        with open(path_file_name, "w") as f:
            print(f)
    with open(path_file_name, "a",encoding='utf-8') as f:
        f.write(url, )

# if __name__ == '__main__':
#     a=create_article_to_txt(123,'choker')
