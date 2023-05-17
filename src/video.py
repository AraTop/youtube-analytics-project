import os
from googleapiclient.discovery import build

class Video:
   api_key: str = os.getenv('API_KEY')
   youtube = build('youtube', 'v3', developerKey=api_key)
   id = None
   title = None
   url = None
   count_views = None
   count_likes = None

   def __init__(self, uid) -> None:
      video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=uid
                                       ).execute() 
      
      self.id = uid
      self.title = video_response['items'][0]['snippet']['title']
      self.url = f"https://www.youtube.com/watch?v={uid}"
      self.count_views = video_response['items'][0]['statistics']['viewCount']
      self.count_likes = video_response['items'][0]['statistics']['likeCount']

   def __str__(self) -> str:
        return f"{self.title}"
   
class PLVideo(Video):
   playlist = None
    
   def __init__(self, uid, playlist) -> None:
      super().__init__(uid) 
      self.playlist = playlist

   def __str__(self) -> str:
        return f"{self.title}"