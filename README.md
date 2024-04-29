# YouTube Video Downloader

This Python script allows you to download YouTube videos in the highest available resolution and merge the video and audio files using FFmpeg.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `pytube` library
- `ffmpeg-python` library
- FFmpeg (installed on your system)

You can install the required Python libraries using pip:

```bash
pip install pytube ffmpeg-python
```

To install FFmpeg on your system, follow the instructions for your operating system:

- **Windows:** Download the FFmpeg binaries from the [official website](https://ffmpeg.org/download.html#build-windows) and add the `bin` directory to your system's PATH environment variable.
- **macOS:** Install FFmpeg using Homebrew by running `brew install ffmpeg` in the terminal.
- **Linux:** Install FFmpeg using your distribution's package manager (e.g., `sudo apt-get install ffmpeg` on Ubuntu or Debian).

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```bash
python youtube_downloader.py
```

4. When prompted, enter the YouTube video link you want to download.

5. The script will display the available video resolutions. Enter the number corresponding to the desired resolution.

6. The script will download the video and audio files separately, merge them using FFmpeg, and save the final video file with the title of the YouTube video in the same directory as the script.

7. Once the download and merging process is complete, you will see a success message.

## Troubleshooting

- If you encounter the error "No such file or directory: 'ffmpeg'", make sure FFmpeg is installed correctly on your system and accessible from the command line. Refer to the prerequisites section for installation instructions.

- If you face any other issues or errors, please check the error message and ensure that you have installed all the required dependencies and have a stable internet connection.

## License

This script is open-source and available under the [MIT License](LICENSE).

## Disclaimer

Please note that downloading YouTube videos may be subject to the terms of service of YouTube. Make sure you have the necessary permissions and comply with the applicable laws and regulations when using this script.

Use this script responsibly and respect the intellectual property rights of content creators.
