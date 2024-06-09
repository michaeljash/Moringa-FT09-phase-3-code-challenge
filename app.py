from models.author import Author
from models.magazine import Magazine
from models.article import Article
from database.setup import create_tables

# Initialize the database
create_tables()

# Create an author
author1 = Author(id=None, name="John Doe")
print(f"Author ID: {author1.id}, Name: {author1.name}")

# Create a magazine
magazine1 = Magazine(id=None, name="Tech Today", category="Technology")
print(f"Magazine ID: {magazine1.id}, Name: {magazine1.name}, Category: {magazine1.category}")
article1 = Article(author=author1, magazine=magazine1, title="The Future of AI")
print(f"Article Title: {article1.title}, Author: {article1.author}, Magazine: {article1.magazine}")


print(f"Articles by {author1.name}: {author1.articles()}")


print(f"Magazines by {author1.name}: {author1.magazines()}")

print(f"Articles in {magazine1.name}: {magazine1.articles()}")


print(f"Contributors to {magazine1.name}: {magazine1.contributors()}")


print(f"Article titles in {magazine1.name}: {magazine1.article_titles()}")


print(f"Contributing authors with more than 2 articles in {magazine1.name}: {magazine1.contributing_authors()}")
