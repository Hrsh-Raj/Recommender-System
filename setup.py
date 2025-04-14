from setuptools import setup, find_packages #find_packages automatically find the data in your source directory __init__ file.

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Edit below variables as per your requirements -
REPO_NAME = 'ML Based Books Recommender System'
AUTHOR_USER_NAME = 'HRSH RAJ'
SRC_REPO = 'books_recommender'
LIST_OF_REQUIREMENTS = []


setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = 'HRSH RAJ',
    description = 'A small local packages for ML based books recommendations',
    long_description = long_description, 
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Hrsh-Raj/Recommender-System', 
    author_email = 'hrshraj001@gmail.com',
    packages = find_packages(), 
    license = 'MIT',
    python_requires = '>=3.7', 
    install_requires = LIST_OF_REQUIREMENTS
)