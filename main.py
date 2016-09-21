from jlpt_bot import JLPTBot
import webapp2


class DryRunHandler(webapp2.RequestHandler):
    def get(self):
        tweet(self.response, dry_run=True)


class TweetHandler(webapp2.RequestHandler):
    def get(self):
        tweet(self.response, dry_run=False)

def tweet(response, dry_run=True):
    bot = JLPTBot()
    msg = bot.format(bot.get_date_based_word())
    if not dry_run:
        bot.tweet(msg)
    response.headers['Content-Type'] = 'text/plain'
    response.write(msg)


application = webapp2.WSGIApplication([
    ('/', DryRunHandler),
    ('/tweet', TweetHandler),
], debug=True)
