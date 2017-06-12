#!/usr/bin/env python

from pyArango.connection import Connection

# connect to the db, the db has been setup via docker with no root password
conn = Connection(username='root')

db = conn['eegleio']

# try creating a 'Users' collection if it doesn't exist
try:
    userCollection = db.createCollection(name='Users')
except Exception as e:
    userCollection = db['Users']


# get name and key for the users that have titouan.creach@eegle.io as an email
GET_USER_QUERY = """
    FOR u in Users
        FILTER u.email == "titouan.creach@eegle.io"
        RETURN {name: u.name, key: u._key}
"""

# create document
document = userCollection.createDocument()
document['name'] = 'titouan'
document['email'] = 'titouan.creach@eegle.io'
document.save()

# execute query
result = db.AQLQuery(GET_USER_QUERY, rawResults=True)

for user in result:
    print('name: {}, key: {}'.format(user['name'], user['key']))

