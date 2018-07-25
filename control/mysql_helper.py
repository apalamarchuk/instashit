import mysql.connector


class MySqlHelper(object):
    select_following = 'SELECT * FROM following_list ORDER BY id;'
    select_followers = 'SELECT * FROM followers_list ORDER BY id;'
    empty_following = 'DELETE FROM following_list;'
    empty_followers = 'DELETE FROM followers_list;'
    set_autoincrement_following = 'ALTER TABLE following_list AUTO_INCREMENT = 1;'
    set_autoincrement_followers = 'ALTER TABLE followers_list AUTO_INCREMENT = 1;'
    insert_following = "INSERT INTO following_list(name) VALUE (%s);"
    insert_follower = "INSERT INTO followers_list(name) VALUE (%s);"
    __cursor = None

    def __init__(self):
        self.cnx = mysql.connector.connect(user='admin', password='admin', host='127.0.0.1', database='instashit')
        self.cnx.autocommit = True
        self.__cursor = self.cnx.cursor()

    def get_cursor(self):
        return self.__cursor

    def print_default_list(self):
        self.__cursor.execute('SELECT * FROM default_list ORDER BY id;')
        for (id, name, time) in self.__cursor:
            print("{}    {}     {}".format(id, name, time))

    def add_to_default_list(self, string):
        self.__cursor.execute(self.insert_following, (string,))

    def delete_default_list(self):
        self.__cursor.execute(self.empty_following)

    def reset_autoincrement_default_list(self):
        self.__cursor.execute(self.set_autoincrement_following)

    def add_to_followers_list(self, string):
        self.__cursor.execute(self.insert_follower, (string,))

    def delete_followers_list(self):
        self.__cursor.execute(self.empty_followers)

    def reset_autoincrement_followers_list(self):
        self.__cursor.execute(self.set_autoincrement_followers)

    def add_to_following_list(self, string):
        self.__cursor.execute(self.insert_following, (string,))

    def delete_following_list(self):
        self.__cursor.execute(self.empty_following)

    def reset_autoincrement_following_list(self):
        self.__cursor.execute(self.set_autoincrement_following)
