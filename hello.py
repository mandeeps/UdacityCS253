import webapp2
import string

form = """
<body>
	<form method="post" action="/redirect">
		<textarea name="text"></textarea>
		<input type="submit"></input>
	</form>
</body>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(form)

class RedirectHandler(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		plain = self.request.get("text")
		crypto = plain.encode('rot13')
		self.response.write(crypto)

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/redirect', RedirectHandler)
], debug=True)