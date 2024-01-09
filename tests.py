import unittest

from party import app
from model import db, example_data, connect_to_db


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(b"board games, rainbows, and ice cream sundaes", result.data)

    def test_no_rsvp_yet(self):
        # Add a test to show we see the RSVP form, but NOT the
        # refer to self.client to make a GET request to our server?
        result = self.client.get("/")
        #did we get status code 200
        self.assertEqual(result.status_code, 200)
        #looking for a form
        self.assertIn(b'form-control', result.data)
        # party details
        #check for party details not being present

        self.assertNotIn(b'<h2>Party Details</h2>', result.data)
        

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={"name": "Jane",
                                        "email": "jane@jane.com"},
                                  follow_redirects=True)
        # Once we RSVP, we should see the party details, but
        # not the RSVP form

        self.assertNotIn(b'form-control', result.data)
        self.assertIn(b'<h2>Party Details</h2>', result.data)

        


class PartyTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database (uncomment when testing database)
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data (uncomment when testing database)
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        # (uncomment when testing database)
        db.session.close()
        db.drop_all()

    def test_games(self):
        #test that the games page displays the game from example_data()
        result = self.client.get("/games")
        self.assertEqual(result.status_code, 200)
        #this assertIn finds the test game in the response data
        self.assertIn(b'<td>Potato Game</td>', result.data)

        


if __name__ == "__main__":
    unittest.main()
