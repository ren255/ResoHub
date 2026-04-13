FROM python:3.12.12
WORKDIR /app

RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    pkg-config \
    graphviz \
    libgraphviz-dev \
    graphviz-dev \
    libpq-dev \        
    zsh \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)" -- -t robbyrussell
RUN chsh -s $(which zsh)

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]