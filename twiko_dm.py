import tweepy
import time

# Replace these with your own API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with the Twitter API using your credentials
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Replace "MESSAGE" with the message you want to send
message = "MESSAGE"

# Replace "FOLLOWERS_FILE" with the path to the file containing the list of followers
with open("FOLLOWERS_FILE", "r") as f:
    # Iterate through the list of followers
    for screen_name in f:
        # Look up the user's ID using their screen name
        user = api.get_user(screen_name=screen_name)

        # Get the user's ID
        user_id = user.id

        try:
            # Send the direct message to the user
            api.send_direct_message(recipient_id=user_id, text=message)
            print(f"Message has been sent successfully to {screen_name}")
        except tweepy.errors.Forbidden as e:
            # User cannot be sent a direct message
            print(f"Cannot send message to {screen_name}")
            continue

        # Sleep for 1 minute to respect the rate limits
        time.sleep(60)
