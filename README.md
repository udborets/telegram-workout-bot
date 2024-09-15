# Navigation

- **[TODO](#todo)** 

- **[Start locally](#start-locally)**

  - **[Install](#install)**

# TODO

***See [TODO.md](./TODO.md)***

# Run locally

## Create .env file

1. add bot token with environment variable name ```BOT_TOKEN```

## Start the app

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