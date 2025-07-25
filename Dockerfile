FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV NLTK_DATA=/usr/share/nltk_data

WORKDIR /app

RUN apt-get update && \
    apt-get install -y poppler-utils libgl1 && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -c "import nltk; nltk.download('punkt', download_dir='/usr/share/nltk_data')"

COPY round2.py .

CMD ["python", "round2.py"]
