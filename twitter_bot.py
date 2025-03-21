import tweepy
import requests
import datetime
import schedule
import time

# Twitter API credentials
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
def twitter_authenticate():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Fetch celebrity birthdays
def fetch_celebrity_birthdays():
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    # Example API/website for fetching birthdays (replace with your source)
    url = f"https://example.com/api/birthdays?date={today_date}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()  # Assuming the API returns JSON
        return data.get("celebrities", [])  # Adjust to your API response format
    except Exception as e:
        print(f"Error fetching birthdays: {e}")
        return []

# Compose and send the tweet
def send_birthday_tweet(api):
    birthdays = fetch_celebrity_birthdays()
    if not birthdays:
        print("No birthdays found for today.")
        return

    # Create a tweet
    tweet = "🎉 Today's Top Celebrity Birthdays 🎂\n\n"
    for celeb in birthdays[:5]:  # Take the top 5 celebrities
        tweet += f"{celeb['name']} ({celeb['age']} years old)\n"

    tweet += "\n#CelebrityBirthdays #DailyUpdates"
    try:
        api.update_status(tweet)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error tweeting: {e}")

# Schedule the bot to run daily
def job():
    api = twitter_authenticate()
    send_birthday_tweet(api)

# Run daily at a specific time (e.g., 9:00 AM)
schedule.every().day.at("09:00").do(job)

print("Twitter bot is running. Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(1)
