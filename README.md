# ResoHub

![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)
![Node.js](https://img.shields.io/badge/-Node.js-339933?logo=Node.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white)
![npm](https://img.shields.io/badge/-npm-CB3837?logo=npm&logoColor=white)

![Vike](https://img.shields.io/badge/-Vike-646CFF?logo=vite&logoColor=white)
![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/-Tailwind%20CSS-38B2AC?logo=tailwind-css&logoColor=white)
![DaisyUI](https://img.shields.io/badge/-daisyui-1AD1A5?logo=daisyui&logoColor=black)
![Biome](https://img.shields.io/badge/-biome-60A5FA?logo=biome&logoColor=black)

![Python](https://img.shields.io/badge/-python-3776AB?logo=python&logoColor=black)
![Django](https://img.shields.io/badge/-django-092E20?logo=django&logoColor=black)
![MinIO](https://img.shields.io/badge/-minio-C72E49?logo=minio&logoColor=black)
![MySql](https://img.shields.io/badge/-mysql-4479A1?logo=mysql&logoColor=black)

## Quick Start

### docker install
windowsの場合WSLとdocker desktop
linuxの場合はdocker

### git install

### clone repo
```sh
git clone https://github.com/ren255/ResoHub/
cd ResoHub/backend
```

### backend初期化
- python 仮想環境構築
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- db初期化
```sh
python manager.py migrate
cd ../
```

# 起動
- 機密設定
  `.evn`を`ResoHub/`へ配置する
- docker 起動 
```sh
docker compose up --build
```

https://localhost:8080 へアクセスすると以下のようなサイトが見れたらOK
https://resohub.rentoda.com
