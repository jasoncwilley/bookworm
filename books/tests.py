from django.test import TestCase

from .models import Author, Book

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.authors = {
            "matt": Author.objects.create(name="Matt"),
            "drew": Author.objects.create(name="Drew"),
            "nick": Author.objects.create(name="Nick"),
            "will": Author.objects.create(name="Will"),
            "lavanya": Author.objects.create(name="Lavanya"),
            "kelly": Author.objects.create(name="Kelly"),
            "brett": Author.objects.create(name="Brett"),
            "jay": Author.objects.create(name="Jay"),
            "jason": Author.objects.create(name="Jason"),
            "anders": Author.objects.create(name="Anders"),
            "gary": Author.objects.create(name="Gary"),
            "thomas": Author.objects.create(name="Thomas"),
            "travis": Author.objects.create(name="Travis"),
        }

        cls.bookshelves = [

        ]

        cls.books = [
            Book.objects.create(title="book 1"),
            Book.objects.create(title="book 2"),
            Book.objects.create(title="book 3"),
            Book.objects.create(title="book 4"),
            Book.objects.create(title="book 5"),
            Book.objects.create(title="book 6"),
            Book.objects.create(title="book 7"),
            Book.objects.create(title="book 8"),
        ]

        cls.books[0].authors.add(cls.authors["matt"])
        cls.books[1].authors.add(cls.authors["nick"])
        cls.books[2].authors.add(cls.authors["anders"])
        cls.books[3].authors.add(cls.authors["matt"], cls.authors["drew"], cls.authors["nick"])
        cls.books[4].authors.add(cls.authors["thomas"], cls.authors["travis"])
        cls.books[5].authors.add(cls.authors["matt"], cls.authors["brett"])
        cls.books[6].authors.add(cls.authors["matt"], cls.authors["lavanya"])
        cls.books[7].authors.add(cls.authors["kelly"])

    def test_number_of_authors(self):
        self.assertEqual(len(self.authors), Author.objects.all().count())

    def test_get_author_by_pk(self):
        author = Author.objects.get(pk=self.authors["nick"].pk)
        self.assertEqual(self.authors["nick"], author)

    def test_get_author_by_name(self):
        author = Author.objects.get(name="Lavanya")

        self.assertEqual(self.authors["lavanya"], author)

    def test_update_author(self):
        author = Author.objects.get(name="Matt")
        author.name = "Matt is tired"
        author.save()

        author_to_check = Author.objects.get(pk=self.authors["matt"].pk)

        self.assertEqual(author_to_check.name, "Matt is tired")

    def test_does_not_exist_error(self):
        self.assertRaises(Author.DoesNotExist, lambda: Author.objects.get(name="Bobby"))

    def test_get_book_authors(self):
        authors = Book.objects.get(title="book 3").authors

        self.assertEqual(authors.count(), 1)
        self.assertEqual(list(authors.all()), [self.authors["anders"]])

        authors = Book.objects.get(title="book 4").authors

        self.assertEqual(authors.count(), 3)
        self.assertEqual(list(authors.all()), [
            self.authors["matt"],
            self.authors["drew"],
            self.authors["nick"],
        ])