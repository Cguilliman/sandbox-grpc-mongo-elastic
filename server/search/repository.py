from elasticsearch_dsl import Q, connections
from storage.schemas import BookDBModel

from .schema import BookEs


class BookSearchService:
    def __init__(self):
        self.es = connections.get_connection()
        if not self.es.indices.exists(index=BookEs.Index.name):
            BookEs.init()

    @staticmethod
    def save(book_model: BookDBModel):
        book = BookEs(
            meta={"id": book_model.id},
            book_id=book_model.id,
            title=book_model.title,
            category=book_model.category,
            updated_at=book_model.updated_at,
        )
        book.save()

    @staticmethod
    def search(search_term: str):
        query = BookEs.search()
        query = query.extra(
            track_scores=True,
            _source={
                "exclude": [
                    "book_id",
                    "category",
                    "updated_at",
                    "added_at",
                ]
            },
        )
        query = query.query(
            Q(
                "match",
                title={
                    "query": search_term,
                },
            )
        )
        return query.execute().hits
