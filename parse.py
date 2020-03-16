import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS testdata (
              Id INTEGER PRIMARY KEY,
              PostTypeId INTEGER PRIMARY KEY,
              ParentId INTEGER PRIMARY KEY,
              AcceptedAnswerId INTEGER PRIMARY KEY,
              CreationDate TEXT,
              Score INTEGER PRIMARY KEY,
              ViewCount INTEGER PRIMARY KEY,
              Body TEXT,
              OwnerUserId INTEGER PRIMARY KEY,
              LastEditorUserId INTEGER PRIMARY KEY,
              LastEdiDate TEXT,
              LastActivityDate TEXT,
              CommentCount INTEGER PRIMARY KEY,
              Title TEXT,
              Tags TEXT,
              AnswerCount INTEGER PRIMARY KEY,
              FavoriteCount INTEGER PRIMARY KEY,
              ClosedDate TEXT,
              OwnerDisplayName TEXT)''')

db.commit()
import xml.etree.ElementTree as ET 

tree = ET.parse('bioinformatics_posts_se.xml')
library = tree.getroot()

test_data = []
for bioinform in library:
    Id, PostTypeId, ParentId, AcceptedAnswerId, CreationDate, Score, ViewCount, Body, OwnerUserId, LastEditorUserId, LastEdiDate, LastActivityDate, CommentCount, Title, Tags, AnswerCount, FavoriteCount, ClosedDate, OwnerDisplayName = ('',) * 19
    t = (Id, PostTypeId, ParentId, AcceptedAnswerId, CreationDate, Score, ViewCount, Body, OwnerUserId, LastEditorUserId, LastEdiDate, LastActivityDate, CommentCount, Title, Tags, AnswerCount, FavoriteCount, ClosedDate, OwnerDisplayName)
    test_data.append(t)

    cursor.execute('''INSERT INTO testdata
    Id, 
    PostTypeId, 
    ParentId, 
    AcceptedAnswerId, 
    CreationDate, 
    Score, 
    ViewCount, 
    Body, 
    OwnerUserId, 
    LastEditorUserId, 
    LastEdiDate, 
    LastActivityDate, 
    CommentCount, 
    Title, 
    Tags, 
    AnswerCount, 
    FavoriteCount, 
    ClosedDate, 
    OwnerDisplayName)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (Id, PostTypeId, ParentId, AcceptedAnswerId, CreationDate, Score, ViewCount, Body, OwnerUserId, LastEditorUserId, LastEdiDate, LastActivityDate, CommentCount, Title, Tags, AnswerCount, FavoriteCount, ClosedDate, OwnerDisplayName) )
db.commit()
catalog = ET.Element('catalog')
from xml.dom import minidom

xml_str = minidom.parseString(ET.tostring(catalog).encode('utf-8')).toprettyxml(indent=" ")

with open("new_data.xml", 'w') as xml_file:
    xml_file.write(xml_str.encode('utf-8'))
