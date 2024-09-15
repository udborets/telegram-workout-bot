# Navigation

- **[TODO](#todo)** 

- **[Run locally](#run-locally)**

  - **[Install](#install)**

# TODO

***See [TODO.md](./TODO.md)***

# Run locally

## 1. Clone repository

```bash
git clone https://github.com/udborets/telegram-workout-bot.git
cd telegram-workout-bot
```

## 2. Create .env file

1. add bot token with environment variable name ```BOT_TOKEN```

## 3. Start the app

### Via Docker

1. Build Docker image

```bash
docker compose build
```

2. Run Docker image

```bash
docker compose up
```

### Via Anaconda

1. Create and activate Anaconda environment

```bash
conda create -n telegram-workout-bot python=3.12 -y
conda activate telegram-workout-bot
```

2. Install Python packages

```bash
pip install -r requrements.txt
```

3. Run main.py

```python
python main.py
```

# Feedback

I would love to hear a feedback about this project!

Feel free to contact me via

- Telegram: [@udborets](https://t.me/udborets)

- Email: [udborets@gmail.com](mailto:udborets@gmail.com)