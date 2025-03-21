import tweepy
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

# Authenticate with Twitter API
client = tweepy.Client(
    consumer_key=os.getenv('API_KEY'),
    consumer_secret=os.getenv('API_SECRET_KEY'),
    access_token=os.getenv('ACCESS_TOKEN'),
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
)

# Function to scrape top celebrity birthdays
def get_top_birthdays():
    # Automatically fetch today's date and construct the URL
    today = datetime.now().strftime("%B-%d").lower()  # Example: "march-21"
    url = f"https://www.famousbirthdays.com/{today}.html"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract top 5 birthdays (adjust based on the site's structure)
    birthdays = []
    for item in soup.select('.name')[:5]:  # Adjust the selector as needed
        birthdays.append(item.text.strip())
    
    return birthdays

# Function to create and post a tweet
def tweet_birthdays():
    birthdays = get_top_birthdays()
    if birthdays:
        # Format the tweet
        tweet = "Today's Top 5 Celebrity Birthdays:\n" + "\n".join(birthdays)
        try:
            # Post the tweet
            client.create_tweet(text=tweet)
            print("Tweet posted successfully!")
        except Exception as e:
            print("Error while tweeting:", e)
    else:
        print("No birthdays found for today.")

# Trigger the tweet function
if __name__ == "__main__":
    tweet_birthdays()
