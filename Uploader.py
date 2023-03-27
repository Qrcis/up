# ========================================== IMPORT ==========================================
try:
    from pyrogram import Client, filters, idle, ContinuePropagation
    from pyrogram.types import Message, InlineKeyboardButton as button, InlineKeyboardMarkup
except ImportError:
    from os import system
    system("python3 -m pip install pyrogram tgcrypto")
    exit("( RUN THE‌ SCRIPT‌ AGAIN )")
from dictdb import db, listdb; steps, files, tedad, links = db("steps"), db("files"), db('tedad'), listdb('links')
from get_config import get_config, get; config = get(get_config())
steps, chats = db("steps"), db("chats")
channels = config.channels.replace(" ", "").split(","); print (channels)
from random import choice
from string import ascii_lowercase, ascii_uppercase; asc = ascii_lowercase+ascii_uppercase+"0987654321"
def creat_link():
    char = ''
    while True:
        for _ in range(10):
            char += choice(asc)
        if files.checkExist(char) == False:
            return char
        else:
            char = ''
# ========================================== START CLIENT ==========================================
name, api_id, api_hash, bot_token = str("o0k"), int(config.api_id), str(config.api_hash), str(config.bot_token)
app = Client(session_name=name, api_hash=api_hash, api_id=api_id, bot_token=bot_token)
with app:
    botU = app.get_me().username
# ========================================== Inline Button ==========================================
in_home = InlineKeyboardMarkup([
        [button("📤", callback_data="Upload"), button(f"فایل های من", callback_data="Myfiles")],
        [button("بستن منو", callback_data="Close")]
        ])
in_get_file = InlineKeyboardMarkup([
        [button("🔙", callback_data="Back")],
        [button(" بستن ", callback_data="Close")]
        ])
def linkss():
    txt = ''
    mylist = []
    for channel in channels:
        if len(channel) >= 5 and channel != "":
            if channel not in mylist:
                txt += f"🔒 @{channel}\n"
        mylist.append(channel)
    return txt
channelss = linkss()

def check_join(app, user_id):
    if channels[0] != '':
        try:
            for channel in channels:
                app.get_chat_member(channel, user_id)
            return True
        except:
            return False
    return True
# ========================================== MAIN CODES ==========================================
@app.on_message(filters.private)
def main_e(app, m: Message):
    if check_join(app, m.from_user.id):
        raise ContinuePropagation
    else:
        m.reply(f"اول بجوین چنل زیر بع  تایید بزن\n{channelss}", reply_markup=InlineKeyboardMarkup([
            [button("تایید", callback_data="Check")]
            ]))
@app.on_message(filters.private&filters.regex(r"/get_.*"), group=0)
def on_get(app, m:Message):
    text ,chat_id = m.text, m.chat.id
    try:
        link = text.split("/get_")[1]
        infom = files.get_data(link).split("-")
        htpl = f'https://t.me/{botU}?start={link}'
        tedad.set_data_save(link, tedad.get_data(link)+1)
        app.copy_message(chat_id, infom[0], int(infom[1]), f"تعداد دانلود » `{tedad.get_data(link)}`)\n__**link**__ » `{htpl}`", reply_markup=InlineKeyboardMarkup([
            [button("( 🔗 Link 🔗 )", url=htpl)]
            ]))
    except (IndexError, AttributeError):
        m.reply("( __**Not Found**__ )")
@app.on_message(filters.private&filters.command("start"), group=0)
def on_message(app, m:Message):
    user_id, command, chat_id = m.from_user.id, m.command, m.chat.id
    steps.set_data(user_id, "Home")
    try:
        link = command[1]
        infom = files.get_data(link).split("-")
        tedad.set_data_save(link, tedad.get_data(link)+1)
        app.copy_message(chat_id, infom[0], int(infom[1]), f"تعداد دانلود» `{tedad.get_data(link)}` )")
    except (IndexError, AttributeError):
        m.reply("( __**Main Menu**__ )", reply_markup=in_home)
@app.on_message(filters.private&(filters.voice | filters.audio | filters.animation | filters.photo | filters.media | filters.sticker | filters.document), group=0)
def get_file(app, m:Message):
    user_id, chat_id, message_id = m.from_user.id, m.chat.id, m.message_id
    if steps.data_is(user_id, "get_file"):
        steps.set_data(user_id, "Home")
        links.add_list(user_id)
        link = creat_link()
        links.add_element(user_id, link)
        tedad.set_data_save(link, 0)
        htpl = f'https://t.me/{botU}?start={link}'
        files.set_data_save(link, f"{chat_id}-{message_id}")
        m.reply(f"لینک دانلود\n( `{htpl}` )", reply_markup=InlineKeyboardMarkup([
            [button("( 🔗 Link 🔗 )", url=htpl)]
            ]))
@app.on_callback_query()
def in_call(app, call):
    data, user_id, message_id, chat_id = call.data ,call.from_user.id, call.message.message_id, call.message.chat.id
    if data == "Upload":
        steps.set_data(user_id, "get_file")
        app.edit_message_text(chat_id, message_id, "برای اپلود رسانه خود را ارسال کنید", reply_markup=in_get_file)
    elif data == "Back":
        steps.set_data(user_id, "Home")
        app.edit_message_text(chat_id, message_id, "منو اصلی", reply_markup=in_home)
    elif data == "Myfiles":
        a, b = 1, ""
        me = [] if type(links.get_elemenet(user_id)) == bool else links.get_elemenet(user_id)
        for i in me:
            b += f"__**{str(a):3}**__: /get_{i}\n"; a += 1
        app.edit_message_text(chat_id, message_id, f"فایل اپلود شده\n{b}", reply_markup=in_get_file)
    elif data == "Close":
        steps.set_data(user_id, "Home")
        app.delete_messages(chat_id, message_id)
    elif data == "Check":
        if check_join(app, user_id):
            steps.set_data(user_id, "Home")
            app.edit_message_text(chat_id, message_id, "منو اصلی", reply_markup=in_home)
        else:
            call.answer("❌")
# ========================================== START CLIENT ==========================================
app.start(), print(f"@{botU} Started..."), idle(), app.stop()
