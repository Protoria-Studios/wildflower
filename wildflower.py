import cv2
import sys
import os


def extract_frames(video_path, output_folder, frame_interval=10):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0
    success = True

    while success:
        # Read a frame from the video
        success, frame = video_capture.read()

        # If the frame was read successfully
        if success and frame_count % frame_interval == 0:
            # Save the frame as an image file
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f'{frame_filename} extracted')

        frame_count += 1

    # Release the video capture object
    video_capture.release()
    print(f"Frames extracted and saved to {output_folder}")


if __name__ == "__main__":

    print(f'working with args: {sys.argv}')
    
    if len(sys.argv) == 4:
        
        input_file = sys.argv[1]
        output_folder = sys.argv[2]
        steps = int(sys.argv[3])
        extract_frames(input_file, output_folder, steps)
        os.system(f'start {output_folder}')
    
    else:
        print('Incorrect args.\nUsage: python wildflower.py <input_file> <output_folder> <steps>')