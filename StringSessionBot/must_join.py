from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from Config import MUST_JOIN


@Client.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"๐จูุฌุจ ุงู ุชุดุชุฑู ูู ููุงุฉ [- ๐๐จ๐ฎ๐ซ๐๐ ๐๐ฎ๐ซ๐ ยป]({https://t.me/so_alfaa}) ุญุชู ุชุชููู ูู ุงุณุชุฎุฏุงู ุงูุฎุฏูู ุจุนุฏ ุงูุงุดุชุฑุงู ูู ุจุถุบุท ุนูู ุงุณุชุงุฑุช ูุฑู ุงุฎุฑู.",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("โ ุงุถูุบุท ููุฃุดุชูุฑุงู ุจุงููููููุงู", url=https://t.me/so_alfaa)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ุงูุง ูุณุช ุงุฏูู ูู ุงูููุงู MUST_JOIN  : {MUST_JOIN} !")
