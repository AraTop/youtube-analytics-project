import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    title = ""
    video_count = 0
    url = ""
    view_count = 0
    subscribe_count = 0

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        
        Channel.title = channel['items'][0]['snippet']['title']
        Channel.video_count = channel['items'][0]['statistics']["videoCount"]
        Channel.url = f"https://www.youtube.com/channel/{channel_id}"
        Channel.view_count = channel['items'][0]['statistics']['viewCount']
        Channel.subscribe_count = channel['items'][0]['statistics']["subscriberCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return json.dumps(channel, indent=2, ensure_ascii=False)
    
    @property
    def channel_id(self):
        return self.channel_id
    
    @channel_id.setter
    def channel_id(self, name):
        if name is None:
            raise Exception("AttributeError: property 'channel_id' of 'Channel' object has no setter")
        
    @classmethod
    def get_service(self):
        return self.youtube
    
    def to_json(self, name_file: str):
        json_str = f'"title":{Channel.title}, "video_count":{Channel.video_count}, "url":{Channel.url}, "view_count":{Channel.view_count}, "subscribe_count":{Channel.subscribe_count}'
        json_obj = json.loads(json_str)
 
        with open(name_file, 'w') as f:
            json.dump(json_obj, f)