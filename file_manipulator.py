# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
# replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。


## 実行例 python3 file_manipulator.py reverse python_practice/data/test.txt python_practice/dump/test-dumb.txt

import sys
        
def reverse(inputpath, outputpath):
    with open(inputpath) as file:
        contents = file.read()
    output = contents[::-1]
    with open(outputpath, 'w') as file:
        file.write(output)

def copy(inputpath, outputpath):
    with open(inputpath) as file:
        contents = file.read()
    with open(outputpath, 'w') as file:
        file.write(contents)

def duplicate_contents(inputpath, n):
    with open(inputpath) as file:
        contents = file.read()
    for i in range(n):
        contents += contents
        with open(inputpath, 'w') as file:
            file.write(contents)

def replace_string(inputpath, needle, newstring):
    with open(inputpath) as file:
        contents = file.read()
    newContents = contents.replace(needle, newstring)
    with open(inputpath, 'w') as file:
        file.write(newContents)
        

if __name__ == '__main__':
    
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    if len(sys.argv) != 4:
        arg3 = sys.argv[3]
    
    if arg1 == 'reverse':
        reverse(arg2, arg3)
    elif arg1 == 'copy':
        copy(arg2, arg3)
    elif arg1 == 'duplicate-contents':
        duplicate_contents(arg2, arg3)
    elif arg1 == 'replace-string':
        replace_string(arg2, arg3, arg4)
    else:
        print('Invalid command')
