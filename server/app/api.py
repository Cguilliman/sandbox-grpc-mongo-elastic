
import typing
from datetime import datetime

import recommendations_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from loguru import logger
from grpc import ServicerContext
from recommendations_pb2 import (
    Book,
    BookCategory,
    BookDeleteRequest,
    BookModifiedResponse,
    BookRecommendation,
    BookSearchRequest,
    BookSearchResponse,
    CreateBookRequest,
    EmptyRequest,
    EmptyResponse,
    RecommendationRequest,
    RecommendationResponse,
    UpdateBookRequest,
)
from services.book_crud import BookCRUDService
from storage.repositories import BookNotExists
from storage.schemas import BookDBModel, BookSaveModel

import grpc


class BooksServicer(recommendations_pb2_grpc.BooksServicer):
    @staticmethod
    def get_timestamp(dt: datetime) -> Timestamp:
        timestamp = Timestamp()
        timestamp.FromDatetime(dt)
        return timestamp

    def build_book_response(self, book: BookDBModel) -> Book:
        return Book(
            id=book.id,
            category=book.category,
            title=book.title,
            created_at=self.get_timestamp(book.created_at),
            updated_at=self.get_timestamp(book.updated_at),
        )

    def Recommend(self, request: RecommendationRequest, context: ServicerContext) -> RecommendationResponse:
        logger.info("Recommend")
        books: typing.List[BookDBModel] = BookCRUDService.get_by_category(
            request.category
        )
        if not books:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not fount")

        return RecommendationResponse(
            books=[self.build_book_response(book) for book in books]
        )

    def Create(self, request: CreateBookRequest, context: ServicerContext) -> Book:
        logger.info("Create")

        book_request = BookSaveModel(
            category=request.category,
            title=request.title,
        )
        book: BookDBModel = BookCRUDService.save_book(book_request)
        return self.build_book_response(book)

    def Update(self, request: UpdateBookRequest, context: ServicerContext) -> Book:
        logger.info("Update")

        book_request = BookSaveModel(
            id=request.id,
            category=request.category,
            title=request.title,
        )
        try:
            book: BookDBModel = BookCRUDService.save_book(book_request)
            return self.build_book_response(book)
        except BookNotExists:
            context.abort(grpc.StatusCode.NOT_FOUND, "Nothing to update")

    def Monitor(self, request: EmptyRequest, context: ServicerContext) -> typing.Iterator[Book]:
        logger.info("Monitor")

        for book in BookCRUDService.new_books_pulling():
            yield self.build_book_response(book)

    def Delete(self, request: BookDeleteRequest, context: ServicerContext) -> EmptyResponse:
        logger.info("Delete")

        try:
            BookCRUDService.delete_book(request.id)
        except BookNotExists:
            context.abort(grpc.StatusCode.NOT_FOUND, "Nothing to delete")
        return EmptyResponse()

    def Search(self, request: BookSearchRequest, context):
        BookCRUDService.search(request.search)
        context.abort(grpc.StatusCode.NOT_FOUND, "Nothing")
        return BookSearchResponse()
