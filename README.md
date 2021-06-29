# impachu
Discord bot for making memes.

The bot can be added to your server [here](https://discord.com/api/oauth2/authorize?client_id=794697319659732992&permissions=0&scope=bot).

## Discord Channel Usage:

Commands:

  **help** -- show help options
  
   `!help`
     
  **impact** -- create basic impact font meme
  
   `!impact <URL> [top_text] [bottom_text]`
   
   **poster** -- create (de)motivational poster meme
   
   `!poster <URL> [top_text] [bottom_text]`

## Setting the Bot up Yourself

Prequisites 
- python3 virtual environment along with all packages specified in `requirements.txt`
- Install impachu package by calling `pip install -e .` in the root directory
- Discord Bot token stored in `.env` file in root directory of repo with the following format:
```
#.env
DISCORD_TOKEN=<Discord Bot Token>
```

To start the bot, call the `run` script in the `bin` folder.

`./bin/run`
