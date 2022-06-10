import clip_client
import jina
from jina import Executor, requests, DocumentArray, Document
import uuid
import sys


def do_something(docs):
    server_url = 'grpc://0.0.0.0:51001'

    da = docs.post(server_url)
    # print(docs[0].uri)
    # print('old match ids', docs[0].matches[:, ('id', 'text')])
    # print('-' * 30)
    # print('new match ids', da[0].matches[:, ('id', 'text')], len(da[0].embedding))
    # print('*' * 30)
    return da


if __name__ == '__main__':
    tag = sys.argv[1]
    # uri = 'https://raw.githubusercontent.com/jina-ai/clip-as-service/main/.github/README-img/Hurst-began-again.png'
    rid = uuid.uuid1()
    da = DocumentArray()
    for _ in range(20):
        da.append(
            Document(
                id=f'{tag}-{_}', text='hello', matches=[Document(text=f'{str(rid)}')]
            )
        )
    do_something(da)