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
        self.__channel_id = channel_id

        channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        
        self.title = channel['items'][0]['snippet']['title']
        self.video_count = channel['items'][0]['statistics']["videoCount"]
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.view_count = channel['items'][0]['statistics']['viewCount']
        self.subscribe_count = channel['items'][0]['statistics']["subscriberCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return json.dumps(channel, indent=2, ensure_ascii=False)
    
    @property
    def channel_id(self):
        return self._channel_id
    
    @channel_id.setter
    def channel_id(self, name):
        if name is None:
            raise Exception("AttributeError: property 'channel_id' of 'Channel' object has no setter")
        
    @classmethod
    def get_service(self):
        return self.youtube
    
    def to_json(self, name_file: str):
        data = {
            "channel_id": self.__channel_id,
            "title": self.title,
            "url": self.url,
            "subscriber_count": self.subscribe_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
 
        with open(name_file, 'w' , encoding="utf-8") as f:
            json.dump(data, f,ensure_ascii=False, indent=2)

    def __str__(self) -> str:
        return f"<{self.title}> (<{self.url}>)"
    
    def __add__(self, other):
        number = self.subscribe_count 
        other_count = other.subscribe_count
        return int(number) + int(other_count)
    
    def __sub__(self, other):
        number = self.subscribe_count 
        other_count = other.subscribe_count
        return int(number) - int(other_count)
    
    def __lt__(self, other):
        return self.subscribe_count < other.subscribe_count
        
    def __gt__(self, other):
        return self.subscribe_count > other.subscribe_count
    
    def __ge__(self, other):
        return self.subscribe_count >= other.subscribe_count
    
    def __le__(self, other):
        return self.subscribe_count <= other.subscribe_count