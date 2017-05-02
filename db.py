import MySQLdb
import random
import string



def get_db():
	db = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='$Mdni00007',
        db='mask'
    )

    return db.cursor()


def generate(n=8):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def authenticate(username, api_key):
	db = get_db()
	response = db.execute('SELECT * FROM sessions WHERE username=? AND api_key=?', (username, api_key))
	if response is not None and len(response) != 0:
		return True
	else:
		return False