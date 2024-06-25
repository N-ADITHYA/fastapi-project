import psycopg2

conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'Adithya1')

cursor = conn.cursor()

def getting_posts():
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    return posts

def get_posts_by_id(id):
    cursor.execute("""select * from posts where id = %s """, str(id),)
    posts = cursor.fetchone()
    return posts

def insert_into_db(values):
    cursor.execute("INSERT INTO posts (title, content, published) values (%s, %s, %s) returning * ", (values.title, values.content, values.published))
    new_posts = cursor.fetchone()
    conn.commit()
    return new_posts

def delete_post(id):
    cursor.execute("""DELETE FROM posts where id = %s returning *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    return {"deleted": deleted_post}

def updating_rows(id,values):
    cursor.execute("""UPDATE posts set title = %s, content = %s, published = %s where id = %s RETURNING * """,(values.title, values.content, values.published, str(id),))
    updated_posts = cursor.fetchone()
    conn.commit()
    return updated_posts