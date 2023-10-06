from datetime import datetime

from elasticsearch_dsl import Date, Document, Integer, Keyword, Text


class BookEs(Document):
    book_id = Text(fields={"keyword": Keyword()}, required=True)
    title = Text(fields={"keywords": Keyword()}, required=True)
    category = Integer(required=True)
    updated_at = Date(default_timezone="UTC", required=True)
    added_at = Date(default_timezone="UTC", required=True)

    class Index:
        name = "books"
        settings = {
            "analysis": {
                "stemmer": {"tokenizer": "standard", "filter": ["lowercase", "stemmer"]}
            }
        }

    def save(self, **kwargs):
        if self.added_at is None:
            self.added_at = datetime.utcnow()
        return super().save(**kwargs)
