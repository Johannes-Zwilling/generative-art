activate_venv: # Activate the virtual environment for python
	source .venv/bin/activate

install:
	pip install -r requirements.txt; \
	pip install -e .

process_video_to_frames:
	python ./scripts/versions/03/video_to_frames.py

process_frames_to_video:
	python ./scripts/versions/03/frames_to_video.py