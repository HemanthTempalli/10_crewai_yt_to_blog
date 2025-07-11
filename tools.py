from crewai_tools import YoutubeChannelSearchTool

# Initialize the YouTube tool to fetch video transcripts from a specific channel
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@krishnaik06'  # Replace with any YT channel handle
)
