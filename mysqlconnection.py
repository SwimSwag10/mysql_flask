# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
  def __init__(self, db):
    # change the user and password as needed
    connection = pymysql.connect(host = 'localhost', # error: localhost cannot run
                                user = 'root', 
                                password = 'root', 
                                db = db,
                                charset = 'utf8mb4',
                                cursorclass = pymysql.cursors.DictCursor,
                                autocommit = True)
    # establish the connection to the database
    self.connection = connection
  # the method to query the database
  def query_db(self, query, data=None):
    with self.connection.cursor() as cursor: # error: TypeError: 'bool' object is not iterable
      try:
        query = cursor.mogrify(query, data)
        print("Running Query:")

        cursor.execute(query, data) # error: TypeError: 'bool' object is not iterable
        if query.lower().find("insert") >= 0:
          # INSERT queries will return the ID NUMBER of the row inserted
          self.connection.commit()
          return cursor.lastrowid
        elif query.lower().find("select") >= 0: # error: TypeError: 'NoneType' object is not iterable
          # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
          result = cursor.fetchall()
          return result
        else: # error: no error when commented out
          # UPDATE and DELETE queries will return nothing
          self.connection.commit()
      except Exception as e: # error: no error when commented out
        # if the query fails the method will return FALSE
        print("Something went wrong", e)
        return False
      finally: # error: no error when commented out
        # close the connection
        self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db): # error: localhost cannot run
  return MySQLConnection(db)