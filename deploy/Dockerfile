FROM python:3.10-alpine as build
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

FROM build AS final
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "bot.py"]
