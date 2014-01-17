import webapp2
import string
import re

form = """
<body>
	<form method="post" action="/rot13">
		<textarea name="text"></textarea>
		<input type="submit"></input>
	</form>
</body>
"""

SignupForm = """
<body>
	<form method="post" action="/signup">
		<p>Username <input name="username"></input></p>
		<p>Password <input type="password" name="password"></input></p>
		<p>Verify <input type="password" name="verify"></input><p>
		<p>Email <input name="email"></input><p>
		<input type="submit"></input>
	</form>
</body>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(form)

class Rot13Handler(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		plain = self.request.get("text")
		crypto = plain.encode('rot13')
		self.response.write(crypto)

class SignupHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(SignupForm)

	def post(self):
		global username
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")
		
		user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
		if user_re.match(username) and password == verify and re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
			self.redirect('/welcome')
		else:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.write(SignupForm)

class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Welcome ' + username)

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/rot13', Rot13Handler),
	('/signup', SignupHandler),
	('/welcome', WelcomeHandler)
], debug=True)