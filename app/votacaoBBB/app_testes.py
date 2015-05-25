import os
import flaskr
import unittest
import tempfile


class FlaskrTestCase (unittest.TestCase):

    def get_db():
        if not hasattr(g, 'sqlite_db'):
            g.sqlite_db = connect_db()
        return g.sqlite_db

    def init_db():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_participants(self):
        rv = self.app.get('/results')

if __name__ == '__main__':
    unittest.main()
