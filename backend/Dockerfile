FROM python:3.12.12
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .

RUN apt-get update 
RUN apt install -yq default-libmysqlclient-dev build-essential pkg-config
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN apt-get install -yq zsh terminator
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)" -- -t robbyrussell

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]