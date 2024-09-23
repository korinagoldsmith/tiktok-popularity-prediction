import requests
import pandas as pd
from config import API_KEY


# Example function to fetch video data
def get_videos(user_id, count=50):
    url = f"https://api.tiktok.com/v1/videos?user_id={user_id}&count={count}&access_token={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Error: {response.status_code}")
        return []


# Example function to collect data for multiple users
def collect_data(user_ids, output_file='data/videos.csv'):
    all_videos = []
    for user_id in user_ids:
        videos = get_videos(user_id)
        all_videos.extend(videos)

    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(all_videos)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")


if __name__ == "__main__":
    user_ids = ["123456789", "987654321"]  # Replace with actual user IDs
    collect_data(user_ids)
