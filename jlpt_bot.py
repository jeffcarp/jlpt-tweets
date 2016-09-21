import json
from datetime import datetime
from google.appengine.ext import ndb
import tweepy

class JLPTBot():

    def __init__(self):
        creds = TwitterCredentials.get_first()
        auth = tweepy.OAuthHandler(creds.API_KEY, creds.API_SECRET)
        auth.set_access_token(creds.ACCESS_TOKEN, creds.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

        with open('vocab-shuffle.json') as file:
            self.words = json.loads(file.read())

    def tweet(self, message):
        assert message
        self.api.update_status(message)

    def get_date_based_word(self, index_override=None):
        now = datetime.utcnow()
        baseline_time = datetime(2013, 12, 1, 0, 0, 0)
        days_since = (now - baseline_time).days
        index = index_override or days_since
        return self.words[index % len(self.words)]

    @classmethod
    def format(cls, word):
        assert word
        # TODO: cls.validate_word(word)
        english = word['english']
        english = english.replace(',', ', ')
        english = english.strip()

        if 'kanji' in word and word['kanji'] != word['hiragana']:
          return u'{0} - {1}\n{2}'.format(word['kanji'], word['hiragana'], english)
        else:
          return u'{0}\n{1}'.format(word['hiragana'], english)
        end

class TwitterCredentials(ndb.Model):
    API_KEY = ndb.StringProperty()
    API_SECRET = ndb.StringProperty()
    ACCESS_TOKEN = ndb.StringProperty()
    ACCESS_TOKEN_SECRET = ndb.StringProperty()

    @classmethod
    def get_first(cls):
        return cls.query().fetch(1)[0]
