'''
Primary Key (PK)
Objective: Uniquely identify each record within a database table.
Example: Every Django model automatically gets a primary key field named id unless otherwise specified
'''
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    # Django automatically adds 'id' as primary key


'''
Foreign Key (FK):
Objective: Establish relationships between models.
Example: A foreign key in Book model referencing Author model.
'''
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)




'''
One-to-One Relationship:
Objective: Ensure each record in one model corresponds to exactly one record in another model.
Example: One-to-one relationship between Author and AuthorProfile
'''
class Author(models.Model):
    name = models.CharField(max_length=100)

class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    biography = models.TextField()

'''
One-to-Many Relationship:
Objective: Each record in one model can be associated with multiple records in another model.
Example: One-to-many relationship between Author and Book
'''
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

'''
Many-to-Many Relationship:
Objective: Many records in one model can be associated with many records in another model.
Example: Many-to-many relationship between Book and Genre
'''
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)

