import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

PREFIX = os.environ.get("COMMAND_PREFIX", "\.")

# Initializes the app with the bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# Listens to incoming messages that start with ".hello"
@app.message(re.compile("^" + PREFIX + "hello"))
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        text=f"Hey there <@{message['user']}>!",
    )


# Start the app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
