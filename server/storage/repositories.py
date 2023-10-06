import typing
from datetime import datetime, timezone

from app.mongo import collection
from bson.objectid import ObjectId
from loguru import logger
from storage.schemas import BookDBModel, BookSaveModel, Categories


class BookNotExists(Exception):
    pass


class BooksRepository:
    @staticmethod
    def get_book(book_id: str) -> BookDBModel:
        document = collection.find_one({"_id": ObjectId(book_id)})
        if not document:
            raise BookNotExists()
        document["id"] = str(document.get("_id"))
        return BookDBModel(**document)

    @staticmethod
    def save_book(book: BookSaveModel) -> BookDBModel:
        book_data = book.model_dump()
        book_id_to_update = book_data.pop("id", None)
        book_data["updated_at"] = datetime.now(tz=timezone.utc)

        if book_id_to_update and len(book_id_to_update) > 0:
            result = collection.update_one(
                {"_id": ObjectId(book_id_to_update)}, {"$set": book_data}
            )
            saved_book_id = book_id_to_update
        else:
            book_data["created_at"] = datetime.now(tz=timezone.utc)
            result = collection.insert_one(book_data)
            saved_book_id = str(result.inserted_id)

        assert result.acknowledged
        book_model = BooksRepository.get_book(saved_book_id)
        return book_model

    @staticmethod
    def get_by_category(category: Categories) -> typing.List[BookDBModel]:
        documents = collection.find({"category": category})
        result = []
        for item in documents:
            book_id = str(item.pop("_id"))
            result.append(BookDBModel(id=book_id, **item))
        return result

    @staticmethod
    def get_by_date_markers(updated_at: datetime) -> typing.List[BookDBModel]:
        logger.info(updated_at)
        documents = collection.find({"updated_at": {"$gt": updated_at}})
        result = []
        for item in documents:
            book_id = str(item.pop("_id"))
            result.append(BookDBModel(id=book_id, **item))
        return result

    @staticmethod
    def delete_book(book_id: str):
        result = collection.delete_one({"_id": ObjectId(book_id)})
        if not result.deleted_count:
            raise BookNotExists()
