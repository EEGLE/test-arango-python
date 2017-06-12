#!/usr/bin/env python

from pyArango.connection import Connection

conn = Connection(username='root')

db = conn['eegleio']

try:
    userCollection = db.createCollection(name='Users')
except Exception as e:
    userCollection = db['Users']

GET_USER_QUERY = """
    FOR u in Users
        FILTER u.email == "titouan.creach@eegle.io"
        RETURN {name: u.name, key: u._key}
"""

document = userCollection.createDocument()

document['name'] = 'titouan'

document.save()

result = db.AQLQuery(GET_USER_QUERY, rawResults=True)

for user in result:
    print('name: {}, key: {}'.format(user['name'], user['key']))


