#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ind2 import Book, Debt, Subscriber


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Author1", "Book1", 2020, "Publisher1", 10.99)
        self.book2 = Book("Author2", "Book2", 2019, "Publisher2", 9.99)

        self.subscriber1 = Subscriber("Ascorbin", "12345")
        self.subscriber2 = Subscriber("Lofanbl4", "54321")

    def test_initialization(self):
        self.assertEqual(self.subscriber1.surname, "Ascorbin")
        self.assertEqual(self.subscriber1.id, "12345")
        self.assertEqual(self.subscriber1.size, Subscriber.MAX_BOOKS)
        self.assertEqual(self.subscriber1.count, 0)

    def test_add_book(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.assertEqual(self.subscriber1.count, 1)

    def test_remove_book(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.subscriber1.remove_book(self.book1)
        self.assertEqual(self.subscriber1.count, 0)

    def test_books_to_return(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.subscriber1.add_book(self.book2, "2024-02-01", "2024-02-28")
        books_to_return = self.subscriber1.books_to_return()
        self.assertEqual(len(books_to_return), 2)

    def test_find_by_author(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        books_by_author = self.subscriber1.find_by_author("Author1")
        self.assertEqual(len(books_by_author), 1)

    def test_find_by_publisher(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        books_by_publisher = self.subscriber1.find_by_publihser("Publisher1")
        self.assertEqual(len(books_by_publisher), 1)

    def test_find_by_year(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        books_by_year = self.subscriber1.find_by_year(2020)
        self.assertEqual(len(books_by_year), 1)

    def test_price_books_to_return(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.subscriber1.add_book(self.book2, "2024-02-01", "2024-02-28")
        total_price = self.subscriber1.price_books_to_return()
        self.assertEqual(total_price, 10.99 + 9.99)

    def test_generate_debt(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        debt = self.subscriber1.generate_debt()
        self.assertIsInstance(debt, Debt)
        self.assertEqual(len(debt.books), 1)

    def test_get_item(self):
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.assertEqual(self.subscriber1[0]["book"], self.book1)
        self.assertRaises(IndexError, lambda: self.subscriber1[10])

    def test_add_subscribers(self):
        # слияние двух подписчиков
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.subscriber2.add_book(self.book2, "2024-02-01", "2024-02-28")
        merged = self.subscriber1 + self.subscriber2
        self.assertEqual(merged.count, 2)

    def test_and_subscribers(self):
        # пересечение книг между двумя подписчиками
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.subscriber2.add_book(self.book1, "2024-02-01", "2024-02-28")
        intersection = self.subscriber1 & self.subscriber2
        self.assertEqual(intersection.count, 1)

    def test_sub_subscribers(self):
        # разницу между книгами двух подписчиков
        self.subscriber1.add_book(self.book1, "2024-01-01", "2024-01-31")
        self.subscriber1.add_book(self.book2, "2024-02-01", "2024-02-28")
        self.subscriber2.add_book(self.book1, "2024-02-01", "2024-02-28")
        difference = self.subscriber1 - self.subscriber2
        self.assertEqual(difference.count, 1)
        self.assertEqual(difference.books[0]["book"], self.book2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
