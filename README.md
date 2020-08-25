# DeadMatterDiscordBot
A Dead Matter server info bot for Discord app.

# Features:
- .players query => returns the amount of players on the Dead Matter Server. Example = .players

And much more! Try `.help` to get a full list of available commands


# Installation
You must host this bot on the server you are hosting the Dead Matter server. First, you will need [`Python 3.8.X`](https://www.python.org/downloads/release/python-385/).

Clone the repo:
```console
$ git clone https://github.com/theflyingjets/DeadMatterDiscordBot
$ cd DeadMatterDiscordBot
```

Copy the bot.py to Dead Matter Dedicated Server\deadmatter\Saved\Logs

Then cd into that location and install discordpy

```console
cd .\Dead Matter Dedicated Server\deadmatter\Saved\Logs
py -3 -m pip install -U discord.py
```

After thats place your token into the script here from the discord bot app site.
```console
client.run('<API Key or token goes here!>')
```

Then connect or bot to the server and give it prems and run it.
```console
python bot.py
```

### Screenshot preview

![screenshot](https://i.imgur.com/mRgaSJA.png)

### Requirements
This order also applies in the startup order.

- [`Python 3.8.X`](https://www.python.org/downloads/release/python-385/)
- [discord.py](https://github.com/Rapptz/discord.py)

## Contributing

Contributions to DeadMatter Discord Bot are always welcome, whether it be improvements to the documentation or new functionality, please feel free to make the change.