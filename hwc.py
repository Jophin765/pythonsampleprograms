book_name = "Python Programming"
member_name = "Jophin"
first_char = book_name[0]
last_char = book_name[-1]
sliced_title = book_name[0:5]
upper_name = book_name.upper()
lower_name = book_name.lower()
title_name = book_name.title()
replaced_name = book_name.replace("Python", "JAVA")
split_name = book_name.split()
stripped_name = member_name.strip()


available_books = ["Python", "Java", "C++"]
issued_books = ["DBMS"]
members = ["Jophin", "Kiran", "Divya"]

available_books.append("HTML")
available_books.insert(1, "CSS")
available_books.remove("HTML")
popped_book = available_books.pop()
available_books.sort()
available_books.reverse()
available_books = ["Python", "Java", "C++"]

uppercase_books = [book.upper() for book in available_books]

categories = ("Programming", "Database", "Networking")
cat1, cat2, cat3 = categories



genres = {"Python", "Java", "C++"}
genres.add("Networking")
genres.remove("Networking")
member_ids = {101, 102, 103}
new_ids = {103, 104, 105}
union_ids = member_ids.union(new_ids)
intersection_ids = member_ids.intersection(new_ids)

library = {101: {"title": "Python", "author": "Alex"}, 102: {"title": "Java", "author": "David"}}

book = {"book_id": 101, "title": "Python Basics", "author": "John"}
book_author = book.get("author")
book.update({"author": "John Smith"})
book.pop("book_id")
book_items = book.items()

valid_dict = {"title": "Python", 101: "Book ID", ("a", "b"): "tuple key works"}


hash_int = hash(101)
hash_tuple = hash(("a", "b"))

book_not_issued = None

print("------ ONLINE LIBRARY MANAGEMENT SYSTEM ------")
print("Available Books:")
print(available_books)
print("\nUppercase Book Names:")
print(uppercase_books)
print("Book Categories:")
print(cat1)
print(cat2)
print(cat3)
print("Unique Genres:")
print(genres)
print("Book Details:")
print(101, "->", library[101])
print("Dictionary Keys:")
print(library.keys())
print("Dictionary Values:")
print(library.values())
print("Book Not Issued:")
print(book_not_issued)
print("Type of None:")
print(type(book_not_issued))
print("Hash Value:")
print(hash("Python"))