from flask import Flask, render_template, session, request
from requests_html import HTMLSession
from random import shuffle
import os, atexit

app = Flask(__name__)
app.secret_key = os.urandom(24)
page_session = HTMLSession()


# close page_session when server is closed
def all_done():
	page_session.close()
	print('Server closed!')

atexit.register(all_done)

def getProjSrc():
	""" 
	get all projects from MadeWithUnity

	Returns:
		the list of contents from all projects

	"""
	print('Sourcing projects available on MadeWithUnity...', end='')

	# get links for projects
	r = page_session.get("https://unity.com/madewith")
	selector = ('#main > div > div > div'
				'> div.views-element-container'
				'> div > div > div > div')
	elements = r.html.find(selector, first=True).find('main')
	links = [e.absolute_links.pop() for e in elements]

	# get contents for projects
	contents = []
	for link in links:
		# get whatever on project page
		p = page_session.get(link)
		text = p.html.find('#main > article', first=True).html
		contents.append(text)

	print('finished')
	return contents

# projects sourced from MadeWithUnity
# currently store some useful content
project_src = getProjSrc()

def getProjList():
	""" 
	get all projects in a list

	Returns:
		All available projects in a list with shuffled order.

	"""
	copy = project_src[:]
	shuffle(copy)
	return copy

"""
Routers
"""
@app.route('/')
def home():
	clientAddr = request.remote_addr

	# reassign the working list if either
	# looping for all projects finished
	# or the client is new
	if (not (clientAddr in session)) or (not session[clientAddr]):
		session[clientAddr] = getProjList()

	if not session[clientAddr]:
		# sanity check
		# won't enter here if getProjSrc works correctly
		raise Excpetion('No project found')

	# pop the next project and render the page
	nextElement = session[clientAddr].pop(0)
	# otherwise no longer update the session
	session.modified = True

	return nextElement


if __name__ == "__main__":
	app.run(debug=True)