import os

import ffmpeg
from pytube import YouTube


def download_youtube_video(link: str):
    """This function downloads a YouTube video and merges the video and audio streams.

    Args:
        link (str): The YouTube video link to download.
    """
    try:
        # Create a YouTube object
        yt = YouTube(link)

        # Get the available video resolutions
        resolutions = []
        for stream in yt.streams.filter(type="video"):
            resolutions.append(stream.resolution)
        resolutions = list(set(resolutions))  # Remove duplicate resolutions

        # Print the available resolutions
        print("Available resolutions:")
        for i, resolution in enumerate(resolutions, start=1):
            print(f"{i}. {resolution}")

        # Ask the user to choose the resolution
        choice = int(
            input("Enter the number corresponding to the desired resolution: ")
        )
        selected_resolution = resolutions[choice - 1]

        # Get the video and audio streams
        video_stream = yt.streams.filter(
            type="video", resolution=selected_resolution
        ).first()
        audio_stream = yt.streams.filter(type="audio").first()

        # Download the video and audio
        print(f"Downloading video: {yt.title}")
        video_file = video_stream.download(filename="video.mp4")
        print(f"Downloading audio: {yt.title}")
        audio_file = audio_stream.download(filename="audio.mp4")

        # Merge the video and audio using ffmpeg
        print("Merging video and audio...")
        output_file = f"{yt.title}.mp4"
        video = ffmpeg.input(video_file)
        audio = ffmpeg.input(audio_file)
        output = ffmpeg.output(
            video,
            audio,
            output_file,
            vcodec="copy",
            acodec="copy",
            strict="experimental",
        )
        ffmpeg.run(output, overwrite_output=True)

        # Remove the temporary video and audio files
        os.remove(video_file)
        os.remove(audio_file)

        print("Video downloaded and merged successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


video_link = "YOUTUBE_VIDEO_LINK"
download_youtube_video(video_link)
