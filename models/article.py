from database.connection import get_connection

class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.create_article()

    def create_article(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)', (self._author.id, self._magazine.id, self._title))
        connection.commit()
        connection.close()

    @property
    def title(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT title FROM articles WHERE author_id=? AND magazine_id=? AND title=?', (self._author.id, self._magazine.id, self._title))
        title = cursor.fetchone()[0]
        connection.close()
        return title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot change the title after the article is instantiated")

    @property
    def author(self):
        return self._author.name

    @property
    def magazine(self):
        return self._magazine.name
