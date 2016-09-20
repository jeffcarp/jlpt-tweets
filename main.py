import days_left_bot
import webapp2


class DryRunHandler(webapp2.RequestHandler):
    def get(self):
        bot = days_left_bot.DaysLeftBot()
        msg = bot.dry_run()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(msg)


class DaysLeftBotHandler(webapp2.RequestHandler):
    def get(self):
        bot = days_left_bot.DaysLeftBot()
        msg = bot.tweet_current_datetime()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(msg)


application = webapp2.WSGIApplication([
    ('/', DryRunHandler),
    ('/days-left-bot', DaysLeftBotHandler),
], debug=True)
