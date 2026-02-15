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

## Best Practices Q&A

**Why should `kubectl apply` not be used in CI?**
Running `kubectl apply` from a CI job bypasses the GitOps model by making live-cluster changes that might drift from the manifest history. It also couples CI permissions tightly to production, increasing blast radius if secrets leak. Instead, CI should publish artifacts/configs while a controller (e.g., Argo CD, Flux) applies them declaratively.

**Why is `latest` a bad Docker tag?**
`latest` is mutable and non-deterministic; different pulls can yield different bits and you cannot audit which code actually ran. Using immutable tags (commit SHA, semantic version) guarantees reproducibility, rollback clarity, and better cache behavior.

**What is the difference between CI and CD?**
CI (Continuous Integration) focuses on building, testing, and validating code whenever developers merge changes. CD (Continuous Delivery/Deployment) automates the promotion of those validated artifacts into environments (staging/prod) once policies are satisfied, often awaiting manual approval (Delivery) or fully automatic (Deployment).

**How does this pipeline support GitOps?**
The workflow builds a container image per commit, tags it with the Git SHA, and pushes it to the registry. That immutable artifact plus the Git history become the single source of truth. A GitOps controller can watch the repo or image tag updates, ensuring clusters converge on the exact state defined in Git without ad-hoc `kubectl` commands.