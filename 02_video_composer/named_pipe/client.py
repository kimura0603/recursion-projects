# 特定の場所に存在する名前付きパイプ（先程作成した server.py によって作られたもの）からデータを読み取るためのクライアント
# プログラムはその後、ループで名前付きパイプをポーリングし、新しいメッセージが送信されるとそれを読み取ります。
import os
import json

# 'config.json'という名前のJSONファイルを読み込みます。
# このファイルには設定情報が格納されています。
config = json.load(open('config.json'))

# configの'filepath'キーで指定されたパスのファイルを読み取りモード('r')で開きます。
f = open(config['filepath'], 'r')

# 名前付きパイプの続きを読みます。
# flagは、パイプが存在する間はTrueとし、パイプが存在しなくなったらFalseにします。
flag = True

while flag:
    # 指定したパスのファイルが存在しない場合、Falseに設定してwhileループを終了します。
    if not os.path.exists(config['filepath']):
        flag = False

    # ファイルからデータを読み込みます。
    data = f.read()

    # データが空でない場合、その内容を出力します。
    if len(data) != 0:
        print('Data received from pipe: "{}"'.format(data))

# パイプが存在しなくなった後、ファイルを閉じます。
# これはリソースを解放するために重要です。
f.close()