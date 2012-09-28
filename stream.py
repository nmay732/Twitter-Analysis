from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import error
from tweepy import TweepError

# Go to http://dev.twitter.com and create an app. 
consumer_key = "96uZUr59ruZ8XALzSuCWBw"
consumer_secret = "vQGEsUw2GApYIOe9LHe4gEPLTej86bc58o6kfq8"
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="809164207-P2gKumcQbU1WyYe44y4w8ajekOlWTpei4HpjZm5v"
access_token_secret="lwwonALGElgNUd9gsbLTmllPwmSx0qMjgnhOSORuvW8"

class Listener(StreamListener):
	def on_status(self, status):
		# Do things with the post received. Post is the status object.
		print status.text
		return True

	def on_error(self, status_code):
			# If error thrown during streaming.
			# Check here for meaning: https://dev.twitter.com/docs/error-codes-responses
		print "ERROR: ",; print status_code
		return True

	def on_timeout(self):
			# If no post received for too long
		return True

	def on_limit(self, track):
			# If too many posts match our filter criteria and only a subset is
			# sent to us
		return True

	def filter(self, track_list):
		while True:
			try:
				self.stream.filter(track=track_list)
			except error.TweepError as e:
				raise TweepError(e)

if __name__ == '__main__':
	l = Listener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)	
	stream.filter(track=['faggot', 'so gay', 'dyke', 'no homo'])
