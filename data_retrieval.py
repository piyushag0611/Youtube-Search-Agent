
from langchain_community.document_loaders import YoutubeLoader


url = "https://www.youtube.com/watch?v=Q4OBx3S0Ysw"
loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
data = loader.load()
data[0].page_content