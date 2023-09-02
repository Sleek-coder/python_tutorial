import pytest 
from mydb import MyDB

@pytest.fixture(scope="module")
def cur():
    print("setting up the db connection object")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    conn.close()
    curs.close()
    print("closing DB connections")

def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123
    
def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom") 
    assert id == 789
