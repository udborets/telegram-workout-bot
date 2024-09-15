# Navigation

- **[TODO](#todo)** 

- **[Start locally](#start-locally)**

  - **[Install](#install)**

# TODO

## ***high priority***

1. <a href="#1">look for free host services<a>

## workout functionality

- [ ] select workout days

  - [ ] choose muscle groups for each workout day
  
- [ ] add excercies per muscle group?

- [ ] add 

- [ ] rate today's workout

  - [ ] 1-10 rate 

  - [ ] text comment  

## communication with user

- [ ] add list of available functions 

- [ ] add user feedback functionality

## notifications

- [ ] add notifications settings

  - [ ] silent mode

  - [ ] turn on/off

- [ ] add notifications about weight updates 

- [ ] add workout tracking

  - [ ] "went to the gym today?" notification

  - [ ] "going to the gym today" notification

## build graphs (weekly)/(monthly)/(on request)

- [ ] weight

- [ ] days off

## tech stuff

- [ ] dockerize

- [ ] where to host database?

- [ ] where to host app

  - free host services - (examples)?

    - are there any?

    - [ ] <a id="1">look for free host services<a>

  - paid host services - (examples)?

    - i am not a millionaire

# Start locally

## Install

### Via Anaconda

1. Create and activate Anaconda environment

``` 
conda create -n telegram-workout-bot python=3.12 -y
conda activate telegram-workout-bot
```

2. Install Python packages

```
pip install -r requrements.txt
```

## Create .env file

1. add bot token with environment variable name ```BOT_TOKEN```