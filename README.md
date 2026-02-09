## Local Test Run

1. Create a virtual environment and install the dependencies:
	```bash
	pip install -r requirements.txt
	playwright install
	```
2. Execute the smoke tests:
	```bash
	pytest
	```

## Docker Workflow

1. Build the image (replace `your-dockerhub-user` with your username):
	```bash
	docker build -t your-dockerhub-user/startpy:latest .
	```
2. Run the tests inside the container:
	```bash
	docker run --rm your-dockerhub-user/startpy:latest
	```
3. Push to Docker Hub:
	```bash
	docker login
	docker push your-dockerhub-user/startpy:latest
	```

Useful environment variables:
- `HEADLESS` (default `1`): set to `0` locally if you want to see the browser UI.