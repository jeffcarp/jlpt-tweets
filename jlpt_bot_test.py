import unittest
from jlpt_bot import JLPTBot
from datetime import datetime

class Words(unittest.TestCase):

    def test_word_list(self):
        bot = JLPTBot()
        self.assertEqual(len(bot.words), 1803)

class Format(unittest.TestCase):

    def test_format_spaces_commas(self):
        bot = JLPTBot()
        word = {
            u'hiragana': u'\u30c1\u30e3\u30f3\u30b9',
            u'english': u'chance,opportunity',
        }
        self.assertEqual(bot.format(word), u'\u30c1\u30e3\u30f3\u30b9\nchance, opportunity')

    def test_format_kanji(self):
        bot = JLPTBot()
        word = {
            u'kanji': u'\u773a\u3081',
            u'hiragana': u'\u306a\u304c\u3081',
            u'english': u'scene,view,prospect,outlook',
        }
        self.assertEqual(bot.format(word), u'\u773a\u3081 - \u306a\u304c\u3081\nscene, view, prospect, outlook')

class GetDateBasedWord(unittest.TestCase):

    def test_returns_word_based_on_date(self):
        bot = JLPTBot()

        now = datetime.utcnow()
        baseline_time = datetime(2013, 12, 1, 0, 0, 0)
        days_since = (now - baseline_time).days
        expected = bot.words[days_since]

        actual = bot.get_date_based_word()
        self.assertEqual(actual, expected)

    def test_index_is_mod_word_list_length(self):
        bot = JLPTBot()

        expected = bot.words[200]
        actual = bot.get_date_based_word(index_override=len(bot.words) + 200)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
