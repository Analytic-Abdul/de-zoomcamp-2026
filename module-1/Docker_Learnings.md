# Docker Workflow & Commands

## My Daily Docker Commands

### Container Management
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Start a container
docker start [container_id]

# Stop a container
docker stop [container_id]

# Remove a container
docker rm [container_id]
```

### Image Management
```bash
# List images
docker images

# Pull an image
docker pull [image_name]

# Remove an image
docker rmi [image_id]
```

### Building & Running
```bash
# Build from Dockerfile
docker build -t [tag_name] .

# Run container with port mapping
docker run -p [host_port]:[container_port] [image_name]

# Run with volume mount
docker run -v [host_path]:[container_path] [image_name]
```

## What I Learned

### Key Insight #1: VMs vs Docker
Virtual machines virtualize the entire OS. Docker shares the host OS kernel and only packages the application and dependencies. This makes containers:
- Lighter (MBs vs GBs)
- Faster to start (seconds vs minutes)
- More portable (consistent across environments)

### Key Insight #2: Container Persistence
Containers are ephemeral by default. Data disappears when you stop them. Solutions:
- **Volumes**: Docker-managed storage that persists
- **Bind mounts**: Direct mapping to host filesystem

### Key Insight #3: Compose > Individual Containers
For multi-container apps, `docker-compose.yml` is essential:
- Define all services in one file
- Start/stop everything with one command
- Automatic networking between containers

## Resources That Helped
- [NotebookLM Video: VM vs Docker](link_when_you_have_it)
- [DataTalks Zoomcamp Week 1](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform)
- Claude Code for real-time CLI assistance

## Next Steps
- [ ] Complete Zoomcamp Module 1 homework
- [ ] Dockerize a Python data pipeline
- [ ] Push custom image to Docker Hub
