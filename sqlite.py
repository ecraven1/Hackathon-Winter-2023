import sqlite3

conn = sqlite3.connect('workout_videos.sqlite')     # create database file
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Workout_Videos')  # clear any existing tables
cur.execute('CREATE TABLE Workout_Videos (id INTEGER, length TEXT, workout_type TEXT, intensity TEXT, video_link TEXT)')    # create table

# insert all database items
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (1, 'short', 'muscle growth', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (2, 'short', 'muscle growth', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (3, 'short', 'muscle growth', 'high', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (4, 'short', 'cardio', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (5, 'short', 'cardio', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (6, 'short', 'cardio', 'high', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (7, 'short', 'full body', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (8, 'short', 'full body', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (9, 'short', 'full body', 'high', 'link'))

cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (10, 'medium', 'muscle growth', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (11, 'medium', 'muscle growth', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (12, 'medium', 'muscle growth', 'high', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (13, 'medium', 'cardio', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (14, 'medium', 'cardio', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (15, 'medium', 'cardio', 'high', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (16, 'medium', 'full body', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (17, 'medium', 'full body', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (18, 'medium', 'full body', 'high', 'link'))

cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (19, 'long', 'muscle growth', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (20, 'long', 'muscle growth', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (21, 'long', 'muscle growth', 'high', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (22, 'long', 'cardio', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (23, 'long', 'cardio', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (24, 'long', 'cardio', 'high', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (25, 'long', 'full body', 'low', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (26, 'long', 'full body', 'medium', 'link'))
cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link) VALUES (?, ?, ?, ?, ?)', (27, 'long', 'full body', 'high', 'link'))

conn.commit()

# database query
array = ['short', 'cardio', 'high']
cur.execute('SELECT id FROM Workout_Videos WHERE length = ? AND workout_type = ? AND intensity = ?', (array[0], array[1], array[2],))

rows = cur.fetchall()

for row in rows:
    print(row)



conn.commit()




conn.close()