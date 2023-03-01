"""
Requests library is one of the integral part of Python for making HTTP
requests to a specified URL. Whether it be REST APIs or Web Scraping,
requests is must to be learned for proceeding further with these technologies.
When one makes a request to a URI, it returns a response. Python requests provides
inbuilt functionalities for managing both the request and response.

"""

import requests

response = requests.get('https://api.github.com/')

print(response)    # <Response [200]>

print(response.content)    # contents of request


#############################################
##########        response methods      #####
#############################################

# Response.headers returns a dictionary of response headers
print(response.headers)
# {'Server': 'GitHub.com', 'Date': 'Wed, 01 Mar 2023 14:29:23 GMT', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding, Accept, X-Requested-With', 'ETag': '"4f825cc84e1c733059d46e76e6df9db557ae5254f9625dfe8e1b09499c449438"', 'x-github-api-version-selected': '2022-11-28', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Type': 'application/json; charset=utf-8', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Content-Encoding': 'gzip', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '57', 'X-RateLimit-Reset': '1677684464', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Used': '3', 'Accept-Ranges': 'bytes', 'Content-Length': '510', 'X-GitHub-Request-Id': 'FFEA:7D35:1A9C2F15:1B0DD2CC:63FF614A'}


# Response.encoding
# response.encoding returns the encoding used to decode response.content.
print(response.encoding)                #utf-8

# response.elapsed
# response.elapsed returns a timedelta object with the time elapsed from sending the request to the arrival of the response.
print(response.elapsed)            # 0:00:01.869380

# response.closed()
# response.close() closed the connection to the server
print(response.close())           # None

# response.content
# response.content  returns the content of the response , in bytes
print(response.content)          # b'{\n  "current_user_url": "https://api.github.com/user",\n  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",\n  "authorizations_url": "https://api.github.com/authorizations",\n  "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",\n  "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",\n  "emails_url": "https://api.github.com/user/emails",\n  "emojis_url": "https://api.github.com/emojis",\n  "events_url": "https://api.github.com/events",\n  "feeds_url": "https://api.github.com/feeds",\n  "followers_url": "https://api.github.com/user/followers",\n  "following_url": "https://api.github.com/user/following{/target}",\n  "gists_url": "https://api.github.com/gists{/gist_id}",\n  "hub_url": "https://api.github.com/hub",\n  "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",\n  "issues_url": "https://api.github.com/issues",\n  "keys_url": "https://api.github.com/user/keys",\n  "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",\n  "notifications_url": "https://api.github.com/notifications",\n  "organization_url": "https://api.github.com/orgs/{org}",\n  "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",\n  "organization_teams_url": "https://api.github.com/orgs/{org}/teams",\n  "public_gists_url": "https://api.github.com/gists/public",\n  "rate_limit_url": "https://api.github.com/rate_limit",\n  "repository_url": "https://api.github.com/repos/{owner}/{repo}",\n  "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",\n  "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",\n  "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",\n  "starred_gists_url": "https://api.github.com/gists/starred",\n  "topic_search_url": "https://api.github.com/search/topics?q={query}{&page,per_page}",\n  "user_url": "https://api.github.com/users/{user}",\n  "user_organizations_url": "https://api.github.com/user/orgs",\n  "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",\n  "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"\n}\n'

# response.cookies returns a cookiejar object with the cookies sent back from the server
print(response.cookies)          # <RequestsCookieJar[]>


# response history
# Response.history returns a list of response objects holding the history of request(url)
print(response.history)   #[]

# response json
# response.json() returns a json object of the result( if not raises error)
print(response.json())       # {'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}', 'notifications_url': 'https://api.github.com/notifications', 'organization_url': 'https://api.github.com/orgs/{org}', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_teams_url': 'https://api.github.com/orgs/{org}/teams', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'topic_search_url': 'https://api.github.com/search/topics?q={query}{&page,per_page}', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}


# response url
# response url returns the URL of the response
print(response.url)           # https://api.github.com/

# response.text
# response.text returns the content of the response , in unicode
print(response.text)         # {"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","label_search_url":"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}","notifications_url":"https://api.github.com/notifications","organization_url":"https://api.github.com/orgs/{org}","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_teams_url":"https://api.github.com/orgs/{org}/teams","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","topic_search_url":"https://api.github.com/search/topics?q={query}{&page,per_page}","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}


# response reason
# Response.request returns the request object that requested this response
print(response.request)         # <PreparedRequest [GET]>

# response.raise_for_status()
# response.raise_for_status() returns an HTTPError object if an error has occured during the process
print(response.raise_for_status())     # None


# response.ok
print(response.ok)      # True

# response.links()
# response.links returns the header links
print(response.links)         # {}





