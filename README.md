# opendrop-agpl
OpenDrop-AGPL は、透明性と自由を最優先に設計された、ミニマルなオープンソース・ファイル共有システムです。  
このプロジェクトは、Webサービスの「SaaSの抜け穴（GPLコードを改変してクラウド提供してもソースを公開しなくてよい問題）」を解消するために、GNU Affero General Public License (AGPL) v3.0 を「あえて」採用しています。  
## 特徴
超軽量バックエンド: FastAPI (Python) を使用した高速な動作。  
プラグアンドプレイ: データベース不要、ローカルストレージで即座に稼働。  
強制的な透明性: ネットワーク越しに利用する全てのユーザーに対し、稼働中のソースコードへの直接アクセスを提供します。  
コピーレフトの遵守: AGPL第13条に基づき、ユーザーが「ソースコードをダウンロード」できる機能を標準実装。  
## クイックスタート
### 前提条件
Python 3.8 以上  
pip（Pythonパッケージマネージャー）  
### セットアップ  
リポジトリをクローンまたはダウンロードします。  
依存関係をインストールします。
```
pip install fastapi uvicorn
```
サーバーを起動します。  
```
uvicorn main:app --reload
```
ブラウザで http://localhost:8000 にアクセスしてください。  
## プロジェクト構造
```
opendrop-agpl/
├── main.py          # バックエンドロジック（AGPLヘッダー付き）
├── LICENSE          # AGPL v3.0 ライセンス全文
├── README.md        # 本ドキュメント
├── static/
│   └── index.html   # UI（ソースコード配布用リンクを常設）
└── uploads/         # アップロードされたファイルの保存先
```
## ライセンスと哲学
なぜ AGPL なのか？  
多くのファイル共有サービスはクローズドソースであり、サーバー側でどのような処理（検閲、トラッキング、データ解析）が行われているか不透明です。  
本システムは GNU AGPL v3.0 の下で公開されています。これは、あなたがこのコードをフォークして独自のWebサービスを立ち上げた場合、その改変したソースコードも同じライセンスで、かつそのサービスの全ユーザーが取得可能な状態にしなければならないことを意味します。  
"The GNU Affero General Public License is designed specifically to ensure that, in such cases, the modified source code becomes available to the community."  
## ソースコードの取得
本システムを利用する全てのユーザーは、UI下部のリンク、または /source-code エンドポイントから、現在サーバーで実行されているソースコード一式をZIP形式で取得する権利を有します。  
## 貢献について
透明性を高めるための改善、セキュリティパッチ、新機能の提案を歓迎します。全ての貢献は AGPL v3.0 の下で管理されます。  
Copyright (C) 2026 Shirasawa Sakuto  
OpenDrop-AGPL is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
