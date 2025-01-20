import sqlite3
from datetime import datetime

def save_media(user_id, filename, file_content):
    conn = sqlite3.connect('media_app.db')
    c = conn.cursor()
    upload_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO media (user_id, filename, upload_date, file) VALUES (?, ?, ?, ?)',
              (user_id, filename, upload_date, file_content))
    conn.commit()
    conn.close()

def get_user_media(user_id):
    conn = sqlite3.connect('media_app.db')
    c = conn.cursor()
    c.execute('SELECT id, filename, upload_date FROM media WHERE user_id = ?', (user_id,))
    files = c.fetchall()
    conn.close()
    return files

def get_media_file(media_id):
    conn = sqlite3.connect('media_app.db')
    c = conn.cursor()
    c.execute('SELECT filename, file FROM media WHERE id = ?', (media_id,))
    file = c.fetchone()
    conn.close()
    return file
