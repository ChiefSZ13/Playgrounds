def create_citation(author, pub_date, title, publisher):
    author_splitted = author.split(" ")
    citation = f'{author_splitted[-1]}, {author_splitted[0][0]}. ({pub_date}) {title}. Published by {publisher}.'
    return citation


print(create_citation("George Orwell", "1949", "1984", "Penguin"))