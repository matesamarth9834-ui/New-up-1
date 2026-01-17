import os

class Config(object):
    BOT_TOKEN = os.environ.get("8539993825:AAGqD0WR79i7vRPNkxtIHBhdeaEnmBXuL1g")
    API_ID = int(os.environ.get("20246426"))
    API_HASH = os.environ.get("77330c674fb1056fa7029a657075d2dc")
    AUTH_USER = os.environ.get('1259896345', '7602994049').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"

