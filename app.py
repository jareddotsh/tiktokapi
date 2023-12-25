from flask import Flask, request, jsonify
import requests
from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("ms_token", None) # get your own ms_token from your cookies on tiktok.com

async def trending_videos(url):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)

        video_info = await api.video(url=url).info()

        print(video_info['desc'])

        return video_info['desc']

app = Flask(__name__)

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        # Get URL from the request data
        url = request.json.get('url')

        # Fetch data from the provided URL
        response = asyncio.run(trending_videos(url))
        print(response)

        # You can customize this part based on the data you want to extract
        # For simplicity, we are just taking the first 100 characters of the response as "txt"
        txt_data = response

        # Create a dummy user for demonstration
        user = {'name': 'John Doe', 'age': 30}

        # Prepare the response JSON
        response_json = {'description': txt_data, "url" : url}

        return jsonify(response_json)

    except Exception as e:
        # Handle exceptions
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
