from moviepy.editor import *
# User must have moviepy library installed

def cut_and_save_video():
    # Get user input for file name, start time, and end time
    file_name = input("Enter the video file name (including extension): ")
    start_time = float(input("Enter the start time (in seconds): "))
    end_time = float(input("Enter the end time (in seconds): "))

    try:
        # Load the video clip
        video_clip = VideoFileClip(file_name)

        # Validate start and end times
        if 0 <= start_time < end_time <= video_clip.duration:
            # Trim the video
            trimmed_clip = video_clip.subclip(start_time, end_time)

            # Save the trimmed video
            output_file = f"trimmed_{file_name}"
            trimmed_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

            print(f"Video successfully trimmed and saved as {output_file}")
        else:
            print("Invalid start or end time. Make sure they are within the video duration.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cut_and_save_video()
