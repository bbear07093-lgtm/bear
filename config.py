import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8729235570:AAHtlsdBhenTt6CYepGxQtjg7Z5gDKaFoEw")
ADMIN_ID = int(os.getenv("ADMIN_ID", "2010030869"))
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://b_j7hf_user:x47pD6012DJYBkcU1DETBkVpEXw3fsxD@dpg-dbl22r8ae00c73cch71g-a.oregon-postgres.render.com/b_j7hf")

# Telethon uchun
API_ID = int(os.getenv("API_ID", "38486800"))
API_HASH = os.getenv("API_HASH", "c5fc7e4d2190b89e5ce8ea01c0369f09")
