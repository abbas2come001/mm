
import sys

from pyrogram import Client

import config

from ..logging import LOGGER


class AlexaBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"بدء تشغيل البوت...")
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "»بدا البوت والان في انتظار انضمام المساعد..."
            )
        except:
            LOGGER(__name__).error(
                "فشل البوت في الوصول الى المجموعة او القناة تاكد من انك قمت بترقيته الى مسؤول"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error("عليك رفع البوت ادمن في القناة او المجموعة")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"تم التشغيل بواسطة  {self.name}")
