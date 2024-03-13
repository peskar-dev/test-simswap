import os

execution_providers = ["cuda", "coreml"]
execution_threads = int(os.getenv("EXECUTION_THREADS", 10))
fps = 30
frame_processors = ["face_swapper"]
log_level = "error"
output_video_encoder = "libx264"
output_video_quality = 35
reference_frame_number = 25
similar_face_distance = 0.85
temp_directory = "./temp"
temp_frame_format = "png"
temp_frame_quality = 0
video_frames_dir = "./video_frames"
