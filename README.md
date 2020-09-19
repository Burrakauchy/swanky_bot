# Swanky Bot

A Discord Bot to make quizzes!

The design is inspired from Swanky Kong, the character from Donkey Kong Country 2 : Diddy's Kong Quest which gives several quizzes to the player all along the game.

## How to use the bot

### Running the bot

Create your own bot via the portal: [https://discord.com/developers]

Rename the file `data/token.template.json` into `data/token.json` and enter the token of your bot.

The bot is written in python3. To run the code, I recommend to create a virtual environment, follow these introductory step to do so: [https://discordpy.readthedocs.io/en/latest/intro.html].

Once you are in your virtual environment, run `python bot.py`.

### How to configure the bot

You have to write your questions in a file `data/questions.json`.

You can configure the bot by modifying fields in `/data/config.json`.
- "prefix" : the prefix used for interacting with Swanky Bot.


