import socket
import json
import threading

# サーバー側の引き算処理関数
def subtract(params):
    return params[0] - params[1]

# 接続されているクライアントソケットを管理するための辞書
client_sockets = {}

# クライアントのリクエストを処理する関数
def handle_client(client_socket, client_id):
    try:
        while True:
            # クライアントからデータを受信
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break  # データが無い場合は接続を終了

            request = json.loads(data)
            request_id = request.get("id")

            # リクエスト内容の検証と処理
            if 'method' in request and 'params' in request and 'id' in request:
                method = request['method']
                params = request['params']
                
                # メソッドに基づく処理
                if method == "subtract":
                    result = subtract(params)
                    response = {
                        "results": str(result),
                        "result_type": "int",
                        "id": request_id
                    }
                else:
                    response = {
                        "error": "Method not found",
                        "id": request_id
                    }
            else:
                response = {"error": "Invalid request format", "id": request_id}

            # レスポンスをクライアントに送信
            if request_id in client_sockets:
                client_sockets[request_id].send(json.dumps(response).encode('utf-8'))
            else:
                print(f"ID {request_id} に紐づくソケットが見つかりませんでした。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        # 接続終了時のクリーンアップ
        client_socket.close()
        if client_id in client_sockets:
            del client_sockets[client_id]
            print(f"クライアント {client_id} のソケットを削除しました。")

# サーバーを開始する関数
def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("サーバーが開始されました。接続を待っています...")

    # 一意性の確保のため、リクエストのIDではなくカウンタを利用。
    client_id_counter = 0  # 各クライアントに割り当てる一意のID

    while True:
        client_socket, address = server_socket.accept()
        print(f"新しいクライアントが接続されました: {address} (ID: {client_id_counter})")
        
        # クライアントごとのIDでソケットを管理
        client_sockets[client_id_counter] = client_socket

        # マルチスレッドにして、クライアントごとにスレッドで処理
        # スレッドを使わない場合、サーバーが1つのクライアントを処理している間に他のクライアントが待機することになり、効率が悪くなる。
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_id_counter))
        client_thread.start()
        
        client_id_counter += 1

if __name__ == "__main__":
    start_server()
