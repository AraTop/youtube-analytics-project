import os
from googleapiclient.discovery import build
from datetime import timedelta

class PlayList:
   title = None
   url = None

   def __init__(self, playlist_id) -> None:
      api_key: str = os.getenv('API_KEY')
      self.youtube = build('youtube', 'v3', developerKey=api_key)
      playlist_videos = self.youtube.playlists().list(
            part='snippet,contentDetails',
            id=playlist_id
        ).execute()
      self.playlist_id = playlist_id
      self.title = playlist_videos['items'][0]['snippet']['title']
      self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
   
   @property
   def total_duration(self):
      playlist_items = []
      next_page_token = None

      while True:
    # Получите список видео из плейлиста
         playlist_response = self.youtube.playlistItems().list(
         part='contentDetails',
         playlistId=self.playlist_id,
         maxResults=50,  # Максимальное количество видео за один запрос
         pageToken=next_page_token
         ).execute()

         playlist_items += playlist_response['items']
         next_page_token = playlist_response.get('nextPageToken')

         if not next_page_token:
            break
      
         video_response = self.youtube.videos().list(
         part='contentDetails',
         id=video_id
         ).execute()

         total_duration = timedelta()

      for item in playlist_items:
         video_id = item['contentDetails']['videoId']

         # Получите информацию о видео
         video_response = self.youtube.videos().list(
         part='contentDetails',
         id=video_id
         ).execute()

         duration = video_response['items'][0]['contentDetails']['duration']
         duration = timedelta(seconds=int(duration[2:-1]))  # Преобразуйте строку в продолжительность времени
         total_duration += duration

      return total_duration
   
   def show_best_video(self):
      playlist_items = []
      next_page_token = None
      while True:
         playlist_response = self.youtube.playlistItems().list(
               part='snippet',
               playlistId=self.playlist_id,
               maxResults=50
         ).execute()

         playlist_items += playlist_response['items']
         next_page_token = playlist_response.get('nextPageToken')

         if not next_page_token:
            break

      video_likes = []
      for playlist_item in playlist_items:
         video_id = playlist_item['snippet']['resourceId']['videoId']

         video_response = self.youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

         video_likes.append({
            'video_id': video_id,
            'title': playlist_item['snippet']['title'],
            'likes': int(video_response['items'][0]['statistics']['likeCount'])
        })
      
      video_likes.sort(key=lambda x: x['likes'], reverse=True)

      return f'https://youtu.be/{video_likes[0]["video_id"]}'