import subprocess
def convert_video_to_h264(input_file, output_file):
    """
    Converts a video to MP4 format with H.264 codec using ffmpeg.

    :param input_file: Path to the input video file.
    :param output_file: Path to the output video file.
    """
    try:
        # Construct the ffmpeg command
        command = [
            "ffmpeg",
            "-i", input_file,       # Input file
            "-vcodec", "libx264",   # Video codec
            "-acodec", "aac",       # Audio codec
            "-strict", "experimental",
            output_file             # Output file
        ]
        # Run the ffmpeg command
        subprocess.run(command, check=True)
        print(f"Video converted successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("ffmpeg not found. Make sure it is installed and in your PATH.")

# Convert the recorded video
input_video = "objects1.mp4"
output_video = "objects.mp4"
convert_video_to_h264(input_video, output_video)