# eコマースウェブサイト

このプロジェクトは、AWSサービスを使用して商品カタログ、カート機能、ユーザー認証付きのeコマースサイトを構築する方法を示します。

## 使用技術

- AWS Amplify
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon Cognito


## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd ecommerce-website
    ```

2. Amplifyプロジェクトの初期化およびデプロイ:
    ```
    cd amplify
    amplify init
    amplify add auth
    amplify add storage
    amplify add api
    amplify push
    ```

3. Lambda関数のデプロイ:
    - AWS Lambdaコンソールで3つの関数（`get_products.py`, `add_to_cart.py`, `checkout.py`）を作成し、それぞれにコードをコピーします。
    - `boto3`ライブラリを含むLambdaレイヤーを作成し、関数にアタッチします。

4. DynamoDBテーブルの作成:
    - `ProductsTable`と`CartTable`の2つのテーブルを作成します。
    - `ProductsTable`は商品データを保存し、`CartTable`はユーザーのカートデータを保存します。

5. S3バケットの作成:
    - 商品画像を保存するためのS3バケットを作成します。

## 使用方法

- 商品カタログを表示し、商品をカートに追加します。
- カートの内容を確認し、チェックアウトを行います。



