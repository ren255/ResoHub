FROM node:22-alpine
WORKDIR /app

# 依存関係のインストール
COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "run", "dev"]
