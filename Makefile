activate_venv: # Activate the virtual environment for python
	source .venv/bin/activate

install:
	pip install -r requirements.txt; \
	pip install -e .

# Creates individual frames from video file
process_video_to_frames:
	python ./scripts/versions/03/video_to_frames.py

# Takes first frame and calculates coordinates for pixel-value sampling
collect_coordinates:
	python ./scripts/versions/03/collect_coordinates.py





# Samples pixel-values at all coordinates of a frame across all frames

# Uses pixel-values of a frame to render new frame ('converts')

# Takes all converted frames and packs them back into a video file
process_frames_to_video:
	python ./scripts/versions/03/frames_to_video.py