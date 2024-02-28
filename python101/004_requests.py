import requests

facebook_response = requests.get('https://google.com')
print(facebook_response)

# Headers
for header_key, header_value in facebook_response.headers.items():
    print(f"{header_key} : {header_value}")

print(facebook_response.elapsed)
print(facebook_response.cookies)
# print(facebook_response.content)
print(facebook_response.text)


# When downloading image, use
# wget <url_of_image> -O <image_file_name>

# OR
# requests.get('image_url')
# with open('image_name', 'wb') as f:
#   f.write(x.content)
# wb -> write byte

# Then uploading an image
# files = {'file': open('image.png', 'rb')}
# response = requests.post('http://sample.com....', files=files)

# ----------------------------

# If sending a get request with auth...
# .get('http....', auth={username,password})
# You will get response in Authorization (if basic auth used)
# Authorization: Basic dXawqev12s2e3
# dXawqev12s2e3 -> this is base64
# echo -ne dXawqev12s2e3 | base64 -d

# ---------------------------

# Session and adding cookies to all requests in a Session

x = requests.Session()
x.cookies.update({'a': 'b'})
print(x.get('http://httpbin.org/cookies').text)
