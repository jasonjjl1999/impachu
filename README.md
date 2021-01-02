# impachu
Discord bot for making memes. (Currently only supports impact font memes)

The bot can be added to your server [here](https://discord.com/api/oauth2/authorize?client_id=794697319659732992&permissions=0&scope=bot).

## Discord Channel Usage:

Commands:

  **help** -- show help options
  
   `!help`
     
  **impachu** -- create basic impact font meme
  
   `!impachu <Image URL> [<Top Text>][<Bottom Text>]`

## Setting the Bot up Yourself

Prequisites 
- python3 environment along with all packages specified in `requirements.txt`
- Discord Bot token stored in `.env` file in root directory of repo with the following format:
```
#.env
DISCORD_TOKEN=<Discord Bot Token>
```

To start the bot, simply run the following command:
`python3 bot.py`
