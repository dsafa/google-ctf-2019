# requires requests and requests-html

from requests_html import HTMLSession
from urllib.parse import urlparse, parse_qs
import time

lat = 51.5710
lon = -0.1925
token = 'gAAAAABdEwKRoX1YphdiX0kwxKSsY6CmxjNt-R5hkwf4-Ohktb7oyZJRkrX-LK5j12wuj_jgSNjY9wG53zrifwIe1OMk23uTX7LJaYzB7gWRPFUBXYqePYLekg4Z2RgMt3HE0ehzP50Y'
url = 'https://drivetothetarget.web.ctfcompetition.com'
inc = 0.0001
is_lat = False

session = HTMLSession()
while True:
    qlat = lat - inc if is_lat else lat
    qlon = lon - inc if not is_lat else lon
    query = {'lat': "{0:.4f}".format(qlat), 'lon': "{0:.4f}".format(qlon), 'token': token}
    r = session.get(url, params=query)
    response_url = urlparse(r.url)
    response_query = parse_qs(response_url.query)

    token = r.html.find('input')[2].attrs['value']

    print(query)

    try:
        response_text = r.html.find('p')[1].text
        print(response_text)

        if response_text.startswith('You tried to travel') or response_text.startswith('Woa, were about to move'):
            # retry last values
            pass
        elif response_text.endswith('You are getting closer…'):
            # update with new values
            lat = float(response_query['lat'][0])
            lon = float(response_query['lon'][0])
        elif response_text.endswith('You are getting away…'):
            if is_lat:
                print("done, {}".format(query))
                exit()
            is_lat = True
    except:
        print('Error. {}'.format(r.html.text))
        print("url: {}".format(r.url))

# states = [0, 1]
# state = 0
# failcount = 0

# last_lat = lat
# last_lon = lon

# session = HTMLSession()
# while True:
#     query = {'lat': str(lat), 'lon': str(lon), 'token': token}
#     print({'lat': lat, 'lon': lon})
#     r = session.get(url, params=query)
#     response_url = urlparse(r.url)
#     response_query = parse_qs(response_url.query)
#     token = response_query['token'][0]

#     try:
#         response_text = r.html.find('p')[1].text
#         print(response_text)
#         print(token)

#         if response_text.startswith('You tried to travel'):
#             failcount += 1
#             if failcount > 2:
#                 failcount = 0
#                 state = (state + 1) % len(states)

#             lat = last_lat
#             lon = last_lon
#         else:
#             failcount = 0
#             last_lat = lat
#             last_lon = lon

#         if states[state] == 0:
#             lon -= inc
#         else:
#             lat -= inc
#     except:
#         print('Error. {}'.format(r.html.text))
#         print("url: {}".format(r.url))

#     time.sleep(1)


# states = [2]
# state = 0
# inc = 0.0005

# last_lat = lat
# last_lon = lon
# failcount = 0

# while True:
#     query = {'lat': str(lat), 'lon': str(lon), 'token': token}
#     print({'lat': lat, 'lon': lon})
#     r = session.get(url, params=query)
#     response_url = urlparse(r.url)
#     response_query = parse_qs(response_url.query)
#     token = response_query['token'][0]

#     try:
#         response_text = r.html.find('p')[1].text
#         print(response_text)
#         print(token)

#         if response_text.startswith('You tried to travel'):
#             failcount += 1
#             if (failcount > 2):
#                 failcount = 0
#                 # inc /= 10

#             state = (state + 1) % len(states)
#             lat = last_lat
#             lon = last_lon
#         else:
#             failcount = 0
#             inc = 0.001
#             last_lat = lat
#             last_lon = lon

#         if states[state] == 1:
#             lat -= inc
#         elif states[state] == 2:
#             lon -= inc
#         elif states[state] == 0:
#             lat -= inc
#             lon -= inc
#     except:
#         print('Error. {}'.format(r.html.text))
#         print("url: {}".format(r.url))

#     input()