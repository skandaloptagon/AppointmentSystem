'''
This program initializes and handles the database functionality.
Any call to the database should go through here.

Author: John Skandalakis
'''

import sqlite3
import logging

# Always use a logger.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DBManager:

    def __init__(self, dbfile):
        logger.info("Initializing the database manager")

        self.conn = sqlite3.connect(dbfile)

        self.c = self.conn.cursor()

        try:
            self.c.execute('''CREATE TABLE appointments
                     (date text, time text, description text)''')
        except:
            logger.warn("The table already exists. Omitting query.")

    def present_appointments(self, query=None):
        '''
        This is the search functionality of the program
        :param query:
        :return:
        '''

        logger.info("Querying db for appointments matching query: {}".format(query))

        if query is None: # A simple query if the user provides no text
            self.c.execute("select * from appointments")
        else: #Search every column
            sql_query = "SELECT * FROM [appointments] " \
                        "WHERE [description] LIKE '%{0}%' " \
                        "OR [date] LIKE '%{0}%' " \
                        "OR [time] LIKE '%{0}%'".format(query)
            self.c.execute(sql_query)

        return self.c.fetchall()

    def add_appointment_to_db(self, date, time, description):
        '''
        This is the logic for adding an appointment to the database
        :param date:
        :param time:
        :param description:
        :return:
        '''
        logger.info("Adding appointment to database. {}-{}: {}".format(date, time, description))
        return self.c.execute("insert into appointments values (?, ?, ?)", (date, time, description))
