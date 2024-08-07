import os
import argparse
import ffmpeg
import yt_dlp
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def download_youtube_video(link: str):
    try:
        logging.info(f"Attempting to access video at {link}")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=False)
            formats = info['formats']

            # Filter video formats and sort by resolution
            video_formats = [f for f in formats if f.get('vcodec') != 'none']
            video_formats.sort(key=lambda x: int(x.get('height', 0)), reverse=True)

            # Print available resolutions
            print("Available resolutions:")
            for i, format in enumerate(video_formats, start=1):
                print(f"{i}. {format['height']}p")

            # Ask user to choose resolution
            choice = int(input("Enter the number corresponding to the desired resolution: "))
            selected_format = video_formats[choice - 1]

            logging.info(f"User selected resolution: {selected_format['height']}p")

            # Download video
            ydl_opts['format'] = f"{selected_format['format_id']}+bestaudio"
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            print(f"Video downloaded successfully as '{info['title']}.{selected_format['ext']}'!")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
        print(f"An unexpected error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Download YouTube video with custom resolution selection.")
    parser.add_argument("url", help="YouTube video URL")
    args = parser.parse_args()

    download_youtube_video(args.url)

if __name__ == "__main__":
    main()
