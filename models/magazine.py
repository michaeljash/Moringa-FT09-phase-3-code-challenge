from database.connection import get_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category
        self.create_magazine()

    def create_magazine(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
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
        cursor.execute('SELECT name FROM magazines WHERE id=?', (self._id,))
        name = cursor.fetchone()[0]
        connection.close()
        return name

    @name.setter
    def name(self, value):
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE magazines SET name=? WHERE id=?', (value, self._id))
        connection.commit()
        connection.close()

    @property
    def category(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT category FROM magazines WHERE id=?', (self._id,))
        category = cursor.fetchone()[0]
        connection.close()
        return category

    @category.setter
    def category(self, value):
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE magazines SET category=? WHERE id=?', (value, self._id))
        connection.commit()
        connection.close()

    def articles(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT title FROM articles
        WHERE magazine_id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return [article[0] for article in articles]

    def contributors(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT DISTINCT authors.name FROM authors
        JOIN articles ON articles.author_id = authors.id
        WHERE articles.magazine_id = ?
        ''', (self._id,))
        authors = cursor.fetchall()
        connection.close()
        return [author[0] for author in authors]

    def article_titles(self):
        articles = self.articles()
        return articles if articles else None

    def contributing_authors(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT authors.id, authors.name, COUNT(articles.id) as article_count
        FROM authors
        JOIN articles ON articles.author_id = authors.id
        WHERE articles.magazine_id = ?
        GROUP BY authors.id
        HAVING article_count > 2
        ''', (self._id,))
        authors = cursor.fetchall()
        connection.close()
        return [author[1] for author in authors] if authors else None
