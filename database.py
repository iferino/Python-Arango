from arango import ArangoClient

client = ArangoClient(hosts='http://212.80.212.197:18529')

db = client.db('ORTODB', username='ortodbadmin', password='0rt0DB@m1n')

if db.has_collection('todo'):
    collection = db.collection('todo')
else:
    collection = db.create_collection('todo')


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document