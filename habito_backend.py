import sqlite3

#FUNCTION TO CREATE TABLES IN DB
def create_table():
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Habits (id INTEGER PRIMARY KEY , title TEXT , streak INTEGER DEFAULT NULL, longest_streak INTEGER DEFAULT NULL , updation_date TEXT DEFAULT NULL , tomorrows_date TEXT DEFAULT NULL)")
    conn.commit()
    conn.close()

#FUNCTION TO CHECK IF HABIT IS ALREADY PRESENT
def chech_habit_if_present(title):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title from Habits")
    for row in cursor:
        if title.casefold() == row[0].casefold():
            conn.close()
            return True
    conn.commit()
    conn.close()
    return False
    
#FUNCTION TO ADD HABIT
def add_habit(title , streak = 1 , longest_streak = 1 , updation_date = 0 , tomorrows_date = 0):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Habits (title , streak , longest_streak , updation_date , tomorrows_date) VALUES (? , ? , ? , ? , ?)" , (title , streak , longest_streak , updation_date , tomorrows_date))
    conn.commit()
    conn.close()

#FUNCTION TO UPDATE HABIT NAME
def update_habit(id , title):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Habits SET title=? WHERE id=?" , (title , id))
    conn.commit()
    conn.close()

#FUNCTION TO GET HABIT DATA TO DISPLAY
def get_habit_data(title):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Habits WHERE title = ?" , (title,))
    row = cursor.fetchone()
    conn.commit()
    conn.close()
    return row

#FUNCTION TO UPDATE STREAK
def update_streak(title , updation_date , tomorrows_date):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Habits SET streak = streak + 1 , updation_date = ? , tomorrows_date = ? WHERE title=?" , (updation_date , tomorrows_date , title))
    conn.commit()
    conn.close()

#FUNCTION TO UPDATE LONGEST STREAK
def update_longest_streak(id , streak):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Habits SET longest_streak = ? WHERE id = ?" , (streak , id))   
    conn.commit()
    conn.close()

#FUNCTION TO RESET STREAK
def reset_streak(id , updation_date , tomorrows_date):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Habits SET streak = 1 , updation_date = ? , tomorrows_date = ? WHERE id=?" , (updation_date , tomorrows_date , id))
    conn.commit()
    conn.close()

#FUNCTION TO FUNCTION TO DELETE HABIT
def delete_habit(id):
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Habits WHERE id=?" , (id,))
    conn.commit()
    conn.close()

#FUNCTION TO VIEW ALL HABITS
def view_all():
    conn = sqlite3.connect("Habito.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title , streak FROM Habits")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


#FUNCTION CALL TO AUTOMATICALLY CREATE TABLES ON RUN
create_table()