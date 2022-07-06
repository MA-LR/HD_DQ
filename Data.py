from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
📟¦مرحبـاً بـك عزيـزي 📬 {}
⚡¦في بــوت استـخـراج جلـسـة
⚡¦استـخـراج تيرمـكـس تليثون
⚡¦وبــايــروجـرام للـمـيــوزك🎧
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة:  [- 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 »）⛧](https://t.me/so_alfaa)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton(text="🔙رجوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton("࿈ ժᥱ᥎ ꪔᥲ️ժᎥ᥉᥆ꪀ", url="https://t.me/MaDyY_y")],
        [
            InlineKeyboardButton("❓¦طـريـقـه الاسـتـخـدام", callback_data="help"),
            InlineKeyboardButton("💾¦مـعـلومـات", callback_data="about")
      ],
        [InlineKeyboardButton("╞. 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .╡", url="https://t.me/so_alfaa")],
    ]


    # Help Message
    HELP = """
**📚¦الاوامــر الـمتـاحـه**
/about - معلومات البوت
/help - طريقه استخدامي
/start - حتى تشغل البوت
/generate - حتى تبدا بأستخراج كود
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**💾¦مـعـلومـات** 
⚡¦بـوت استخـراج كـود تيرمكـس خـاص بســورس التليـثون وكــود بـايــروجـرام خـاص بـسـورس الـمـيـوزك🎶

🌀¦قـنـاه الـبـوت : [- 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 »](https://t.me/so_alfaa)

🌏¦اللـغــه : [بـايـثـون](www.python.org)

👨🏼‍💻¦الـمـبـرمــج : @MaDyY_y
    """
