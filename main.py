from InstaFollower import InstaFollower
import os
USER_NAME = os.environ['USER_NAME']
PASSWORD = os.environ['PASSWORD']
ACCOUNT_NAME = 'apple'
instaFollowers = InstaFollower()

instaFollowers.login(USER_NAME, PASSWORD)

instaFollowers.find_followers(ACCOUNT_NAME)

instaFollowers.start_following()