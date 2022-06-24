import os
from pyrogram import Client
from bot import Config, LOGGER, USER

plugins = dict(
    root="bot/modules"
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "4GIGSBOT",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.TG_BOT_TOKEN,
            plugins=plugins,
            workdir=Config.WORK_DIR
        )

    async def start(self):
        await super().start()
        await USER.start()
        LOGGER.info("Bot Started...... Now Enjoy")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info('Exiting User........')
        await USER.stop()
        LOGGER.info('Bot and User Exited Successfully ! Bye..........')

if __name__ == "__main__":
    if not os.path.isdir(Config.DOWNLOAD_BASE_DIR):
        os.makedirs(Config.DOWNLOAD_BASE_DIR)
    app = Bot()
    app.run()
