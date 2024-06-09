from database.connection import get_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.create_author()

    def create_author(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        connection.commit()
        self._id = cursor.lastrowid
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT name FROM authors WHERE id=?', (self._id,))
        name = cursor.fetchone()[0]
        connection.close()
        return name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot change the name after author is instantiated")

    def articles(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT title FROM articles
        JOIN authors ON articles.author_id = authors.id
        WHERE authors.id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return [article[0] for article in articles]

    def magazines(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT DISTINCT magazines.name FROM magazines
        JOIN articles ON articles.magazine_id = magazines.id
        WHERE articles.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        connection.close()
        return [magazine[0] for magazine in magazines]
