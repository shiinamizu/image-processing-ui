# slim系のnodeから構築することを定義
FROM node:21.7.3
# コンテナ内の作業ディレクトリを作成
WORKDIR /app
COPY . .
# パッケージ一覧(インデックス)を更新
RUN apt update \
    && yarn install\
	&& npm install axios\
    && npm install clsx\
    && npm install buffer
