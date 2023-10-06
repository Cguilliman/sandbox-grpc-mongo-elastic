import os

from icecream import ic
from recommendations_pb2 import (
    Book,
    BookCategory,
    BookDeleteRequest,
    BookSearchRequest,
    CreateBookRequest,
    EmptyRequest,
    RecommendationRequest,
    UpdateBookRequest,
)
from recommendations_pb2_grpc import BooksStub

import grpc


recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
ic(recommendations_host)
channel = grpc.insecure_channel(f"{recommendations_host}:50051")


def recommendation():
    category = int(input("category (int): "))
    recommendations_entity = BooksStub(channel).Recommend(
        RecommendationRequest(category=category)
    )
    ic(recommendations_entity)


def create():
    modified_entity = BooksStub(channel).Create(
        CreateBookRequest(category=BookCategory.SCIENCE_FICTION, title="New title")
    )
    ic(modified_entity)


def update():
    book_id = str(input("book id (str): "))
    while True:
        category_id = int(input("Category id (0, 1, 2): "))
        if category_id not in (0, 1, 2):
            continue
        else:
            break
    title = str(input("Title: "))
    updated_entity = BooksStub(channel).Update(
        UpdateBookRequest(
            id=book_id,
            category=category_id,
            title=title,
        )
    )
    ic(updated_entity)


def delete():
    book_id = str(input("book id (str): "))
    BooksStub(channel).Delete(
        BookDeleteRequest(
            id=book_id,
        )
    )


def monitor():
    for i in BooksStub(channel).Monitor(EmptyRequest()):
        ic(i)


def search():
    BooksStub(channel).Search(BookSearchRequest(search="new"))


ACTIONS_MAP = {
    "c": create,
    "u": update,
    "r": recommendation,
    "d": delete,
    "m": monitor,
    "s": search,
}


while True:
    action_short = str(input("select action: "))
    if action_short == "e":
        break
    elif action_short not in ACTIONS_MAP:
        continue
    action = ACTIONS_MAP.get(action_short)
    try:
        action()
    except Exception as e:
        ic(e)
