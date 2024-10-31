import socket
import json

# サーバー側の引き算処理関数
def subtract(params):
    return params[0] - params[1]

# サーバーを開始する関数
def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("サーバーが開始されました。接続を待っています...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"クライアントが接続されました: {address}")
        
        try:
            # クライアントからデータを受信
            data = client_socket.recv(1024).decode('utf-8')
            request = json.loads(data)
            
            # リクエスト内容の検証
            if 'method' in request and 'params' in request and 'id' in request:
                method = request['method']
                params = request['params']
                request_id = request['id']
                
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
                response = {"error": "Invalid request format"}

            # レスポンスをクライアントに送信
            client_socket.send(json.dumps(response).encode('utf-8'))
        
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            error_response = {
                "error": str(e),
                "id": request.get('id', None)
            }
            client_socket.send(json.dumps(error_response).encode('utf-8'))
        
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
