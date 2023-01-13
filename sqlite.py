import sqlite3

conn = sqlite3.connect('workout_videos.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Workout_Videos')
cur.execute('CREATE TABLE Workout_Videos (id INTEGER, length FLOAT, workout_type TEXT, intensity TEXT, video_link TEXT)')

cur.execute('INSERT INTO Workout_Videos (id, length, workout_type, intensity, video_link VALUES ()')





conn.close()