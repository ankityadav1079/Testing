FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip ffmpeg git && \
        rm -rf /var/lib/apt/lists/*

        WORKDIR /app

        COPY requirements.txt .
        RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

        COPY . .

        EXPOSE 8000

        CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]