from moviepy.editor import VideoFileClip


def compress_video(input_file, output_file, resolution=(1280, 720), bitrate="500k"):
    clip = VideoFileClip(input_file)
    clip_resized = clip.resize(resolution)  # Resize the video
    clip_resized.write_videofile(output_file, bitrate=bitrate)


# Example usage
compress_video('video.mp4', 'output_video.mp4',
               resolution=(1280, 720), bitrate="500k")
