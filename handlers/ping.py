# Copyright (C) 2020-2021 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime
from pyrogram.types import Message
from callsmusic import callsmusic, Message


@Client.on_message(command("ping")  
about={
    'header': "check how long it takes to ping your userbot",
    'flags': {'-a': "average ping"}}, group=-1)
async def pingme(message: Message):
    start = datetime.now()
    await message.edit('`𝗣𝗼𝗻𝗴!`')
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**𝗣𝗼𝗻𝗴!**\n`{m_s} ms`")
