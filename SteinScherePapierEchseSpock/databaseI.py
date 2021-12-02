import sqlite3
import gamelogic_a
def create_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        sqlite_table_query = ''' Create table if not exists game_outputs (
                                 id INTEGER Primary key,
                                 user TEXT not null,
                                 pc TEXT not null,
                                 game TEXT not null);'''
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_table_query);
        conn.commit()
        print("SQLlite table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def insert(db_file, userinput, aiinput, result):
    conn = sqlite3.connect(db_file)
    sql = ''' INSERT INTO game_outputs(user,pc,game)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    game = (userinput, aiinput, result)
    cur.execute(sql, game)
    conn.commit()
    cur.close()
    conn.close()

def selectResult(db_file):
    conn = sqlite3.connect(db_file)
    sqlWin = "select count(game) from game_outputs where game = 'win'"
    sqlLose = "select count(game) from game_outputs where game = 'lose'"
    sqlDraw = "select count(game) from game_outputs where game = 'draw'"
    cur = conn.cursor()
    cur.execute(sqlWin)
    rowsWins = cur.fetchall()
    cur.execute(sqlLose)
    rowsLose = cur.fetchall()
    cur.execute(sqlDraw)
    rowsDraw = cur.fetchall()
    cur.close()
    conn.close()
    #rows = rowsWins + rowsLose + rowsDraw
    #for row in rows:
    #    print(row)
    print("Wins:", rowsWins,"Lose:",rowsLose,"Draw:",rowsDraw)

def selectUser(db_file):
    conn = sqlite3.connect(db_file)
    sql = "select user from game_outputs group by user order by user limit 1"
    sqlCount = "select count(user) from game_outputs group by user order by user limit 1"
    cur = conn.cursor()
    cur.execute(sql)
    rowUser = cur.fetchall()
    cur.execute(sqlCount)
    rowCount = cur.fetchall()
    cur.close()
    conn.close()
    print("Most used by AI:",rowUser,"How often used by PC:", rowCount)

def selectAI(db_file):
    conn = sqlite3.connect(db_file)
    sql = "select pc from game_outputs group by pc order by pc limit 1"
    sqlCount = "select count(pc) from game_outputs group by pc order by pc limit 1"
    cur = conn.cursor()
    cur.execute(sql)
    rowPc = cur.fetchall()
    cur.execute(sqlCount)
    rowCount = cur.fetchall()
    cur.close()
    conn.close()
    print("Most used by AI:",rowPc,"How often used by PC:", rowCount)