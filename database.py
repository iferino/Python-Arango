from arango import ArangoClient
from model import Todo

client = ArangoClient(hosts='http://212.80.212.197:18529')

db = client.db('ORTODB', username='ortodbadmin', password='0rt0DB@m1n')

if db.has_collection('todo'):
    todos = db.collection('todo')
else:
    todos = db.create_collection('todo')



def fetch_all_todos():
    todoList = []
    for todo in todos:
        todoList.append(Todo(**todo))
    return todoList

def fetch_one_todo(title):
    for todo in todos.find({'title':title}):
        return todo

def create_todo(todo):
    result = todos.insert(todo)
    return todos.get(result['_key'])

def update_todo(title, desc):
    todos.update_match({'title': title}, {'description': desc})
    for doc in todos.find({'title':title}):
        return doc

def remove_todo(title):
    todos.delete_match({'title':title})
    return True