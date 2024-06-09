from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    author1 = Author(id=None, name="John Doe")
print(f"Author ID: {author1.id}, Name: {author1.name}")

# Create a magazine
magazine1 = Magazine(id=None, name="Tech Today", category="Technology")
print(f"Magazine ID: {magazine1.id}, Name: {magazine1.name}, Category: {magazine1.category}")

# Create an article
article1 = Article(author=author1, magazine=magazine1, title="The Future of AI")
print(f"Article Title: {article1.title}, Author: {article1.author}, Magazine: {article1.magazine}")

# List articles by author
print(f"Articles by {author1.name}: {author1.articles()}")

# List magazines by author
print(f"Magazines by {author1.name}: {author1.magazines()}")

# List articles in magazine
print(f"Articles in {magazine1.name}: {magazine1.articles()}")

# List contributors to magazine
print(f"Contributors to {magazine1.name}: {magazine1.contributors()}")

# List article titles in magazine
print(f"Article titles in {magazine1.name}: {magazine1.article_titles()}")

# List contributing authors with more than 2 articles
print(f"Contributing authors with more than 2 articles in {magazine1.name}: {magazine1.contributing_authors()}")