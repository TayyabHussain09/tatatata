import sqlite3

def check_media():
    conn = sqlite3.connect('media_app.db')
    c = conn.cursor()
    # Query to fetch all rows from the media table
    c.execute('SELECT id, user_id, filename, upload_date FROM media')
    rows = c.fetchall()
    conn.close()

    if rows:
        print("Media files stored in the database:")
        for row in rows:
            print(f"Media ID: {row[0]}, User ID: {row[1]}, Filename: {row[2]}, Upload Date: {row[3]}")
    else:
        print("No media files found in the database.")

check_media()
