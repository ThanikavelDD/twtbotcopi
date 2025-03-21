import tweepy
import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twitter API credentials
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
def twitter_authenticate():
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        logging.info("Authenticated with Twitter API successfully.")
        return api
    except Exception as e:
        logging.error(f"Authentication failed: {e}")
        raise

# Fetch celebrity birthdays (placeholder data for testing)
def fetch_celebrity_birthdays():
    logging.info("Fetching placeholder celebrity birthdays...")
    # Placeholder data
    birthdays = [
        {"name": "Celebrity A", "age": 30},
        {"name": "Celebrity B", "age": 40},
        {"name": "Celebrity C", "age": 25},
        {"name": "Celebrity D", "age": 50},
        {"name": "Celebrity E", "age": 35}
    ]
    logging.info(f"Fetched {len(birthdays)} birthdays from placeholder data.")
    return birthdays

# Compose and send the tweet
def send_birthday_tweet(api):
    birthdays = fetch_celebrity_birthdays()
    if not birthdays:
        logging.warning("No birthdays found for today.")
        return

    # Compose the tweet
    tweet = "🎉 Today's Top Celebrity Birthdays 🎂\n\n"
    for celeb in birthdays[:5]:  # Take the top 5 celebrities
        tweet += f"{celeb['name']} ({celeb['age']} years old)\n"

    tweet += "\n#CelebrityBirthdays #DailyUpdates"

    # Post the tweet
    try:
        api.update_status(tweet)
        logging.info("Tweet posted successfully.")
    except Exception as e:
        logging.error(f"Error posting tweet: {e}")

# Execute the bot immediately
if __name__ == "__main__":
    api = twitter_authenticate()
    send_birthday_tweet(api)
