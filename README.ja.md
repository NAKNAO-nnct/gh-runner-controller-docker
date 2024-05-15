## Docker版 GitHub Actions Self-Hosted Runner Controller
このプロジェクトはGitHub ActionsのSelf-Hosted Runnerのコントローラーです。
公式版はKubernetes（k8s）のみをサポートしていますが、Dockerのみを使用する簡易版です。

## セットアップ
1. Docker のインストール
1. git clone
2. .envファイルの編集
3. docker compose up -d
4. Webhookの登録。コントローラを起動した後、エンドポイントをGitHubのWebhookに登録する必要があります。グローバルに直接アクセスできない場合は、Cloudflare Tunnel や ngrok などを利用してください。

## LICENSE
MITライセンス
