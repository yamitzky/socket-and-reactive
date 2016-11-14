# Socket-and-Reactive Experiment Environment

WebsocketとReactiveなビューライブラリを使った実験／プロトタイピング環境のサンプルです。

## Running Development Server

```
docker-compose up
```

http://127.0.0.1:8081/ を開くと開発環境が起動します

## Inside docker-compose

docker-compose.yml は、次の項目によってできています。

- frontend: Webpack ベースの開発サーバーです。vue-cli を使って生成したもので、Vue.js を使っています。
- api: flask ベースのWebsocket のサーバーです。
- db: MongoDB ベースのデータベース・サーバーです。
- gui: mongo-express を使ったMongoDB のGUI 環境です。

このうち最低限必要なものはfrontend とapi です。現在はVue.js とpython(flask) によって構成されていますが、好きな組み合わせで構いません。
