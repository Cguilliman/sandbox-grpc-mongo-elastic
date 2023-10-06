FROM python:3.11.4

RUN mkdir /service
COPY pyproject.toml ./poetry.lock /service/client/
COPY protobufs/ /service/protobufs/
COPY client/ /service/client/
WORKDIR /service/client

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=./ --grpc_python_out=./ ../protobufs/recommendations.proto

ENTRYPOINT ["python", "main.py" ]
