const net = require('net');

// サーバーに接続し、リクエストを送信する関数
function sendRequest(method, params, requestId) {
    const client = new net.Socket();
    const request = {
        method: method,
        params: params,
        id: requestId
    };

    client.connect(12345, 'localhost', () => {
        console.log('サーバーに接続しました');
        // リクエストをJSONに変換して送信
        client.write(JSON.stringify(request));
    });

    client.on('data', (data) => {
        // サーバーからのレスポンスを受信
        const response = JSON.parse(data);
        console.log('サーバーからのレスポンス:', response);
        client.destroy(); // 接続を終了
    });

    client.on('close', () => {
        console.log('接続が閉じられました');
    });

    client.on('error', (err) => {
        console.error('エラーが発生しました:', err.message);
    });
}

// リクエストを送信
sendRequest("subtract", [42, 23], 1);
