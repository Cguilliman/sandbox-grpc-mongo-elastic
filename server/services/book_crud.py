import time
import typing
from datetime import datetime, timezone

from loguru import logger
from search.repository import BookSearchService
from storage.repositories import BooksRepository
from storage.schemas import BookDBModel, BookSaveModel, Categories


class BookCRUDService:
    @staticmethod
    def save_book(book: BookSaveModel) -> BookDBModel:
        saved_book: BookDBModel = BooksRepository.save_book(book)
        BookSearchService().save(saved_book)
        return saved_book

    @staticmethod
    def get_by_category(category: Categories) -> typing.List[BookDBModel]:
        return BooksRepository.get_by_category(category)

    @staticmethod
    def new_books_pulling() -> typing.Iterator[BookDBModel]:
        marker = datetime.now(tz=timezone.utc)
        for _ in range(120):
            for book in BooksRepository.get_by_date_markers(
                marker
            ):  # type: BookDBModel
                yield book
                marker = book.updated_at
            time.sleep(1)

    @staticmethod
    def delete_book(book_id: str):
        BooksRepository.delete_book(book_id)
        # TODO: delete from elastic as well

    @staticmethod
    def search(term: str):
        res = BookSearchService().search(term)
        logger.info(res)

    @staticmethod
    def index_all():
        from storage.repositories import BookDBModel, collection

        search_service = BookSearchService()
        for i in collection.find({}):
            i["id"] = str(i.get("_id"))
            book = BookDBModel(**i)
            search_service.save(book)
