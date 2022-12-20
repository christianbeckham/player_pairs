FROM python:alpine3.17
WORKDIR /home/player_pairs
COPY . .
CMD ["python3", "main.py"]