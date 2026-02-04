# Data Engineering Zoomcamp 2026 - Learning Context Summary

## Course Context
**Program**: DataTalksClub Data Engineering Zoomcamp 2026  
**Repository**: https://github.com/DataTalksClub/data-engineering-zoomcamp  
**Current Module**: Module 1 - Docker & Terraform  
**Learning Environment**: Windows (Git Bash/MINGW64), Docker Desktop  
**Project Directory**: `~/repos/de-zoomcamp-2026/module-1/`

## Your Background & Learning Style
- **Current Skills**: Python and SQL proficient
- **New Territory**: Docker, Git, Terraform, GCP, workflow orchestration, data warehousing
- **Learning Approach**: Hands-on, experimental, prefers understanding "why" before "how"
- **Challenge Areas**: Software engineering fundamentals, terminology, command-line tools
- **Preferences**: Detailed explanations with visual diagrams, breaking down complex concepts into simpler analogies

## Module 1 Progress Overview

### ✅ Completed Topics

#### 1. **Software Development Fundamentals**
- **Git & Version Control**
  - Basic workflow: `git add`, `git commit`, `git push`, `git pull`
  - Understanding repositories, commits, and version history
  - Set up personal repo structure
  
- **Command Line Basics**
  - Terminal/Bash navigation (`cd`, `ls`, `pwd`, `mkdir`)
  - File operations (`touch`, `nano`, `cat`, `echo`)
  - Understanding `~` (home directory), `.` (current directory)
  - Path concepts (absolute vs relative)
  - Line continuation with backslash `\`

- **Python Virtual Environments**
  - Problem: Dependency conflicts between projects
  - Solution: Isolated environments using `uv` (modern package manager)
  - Commands: `python -m uv init`, `python -m uv add`, `python -m uv run`
  - Understanding `.venv` folders and project isolation

#### 2. **Docker Fundamentals**

**Core Concepts Mastered:**
- **Images vs Containers**
  - Image = Blueprint/recipe (static, frozen)
  - Container = Running instance of image (alive, temporary)
  - Dockerfile = Instructions to build an image
  
- **Key Docker Commands**
  ```bash
  docker run          # Create and start container
  docker run -it      # Interactive mode with terminal
  docker run --rm     # Auto-delete container on exit
  docker ps           # List running containers
  docker ps -a        # List all containers
  docker stop <id>    # Stop container
  docker rm <id>      # Remove container
  docker images       # List images
  docker build -t name .  # Build image from Dockerfile
  docker system df    # Check storage usage
  ```

- **Important Flags Learned**
  - `-it`: Interactive terminal access
  - `--rm`: Remove container after exit (useful for temporary tasks)
  - `-e VAR=value`: Set environment variables
  - `-v path:path`: Mount volumes (data persistence)
  - `-p host:container`: Port mapping
  - `--entrypoint`: Override default startup command

**Critical Realizations:**
1. Containers are **stateless** - data disappears when container dies unless using volumes
2. With `--rm`, ALL changes inside container are lost on exit
3. Base images like `python:3.9-slim` already have Python installed
4. Each `docker run` creates a NEW container (even from same image)

#### 3. **Docker Volumes (Data Persistence)**

**Two Types of Volumes:**
1. **Named Volumes** (Docker manages location)
   ```bash
   -v volume_name:/container/path
   # Example: -v ny_taxi_postgres_data:/var/lib/postgresql/data
   ```
   - Docker stores data somewhere safe
   - Survives container deletion
   - Good for databases
   
2. **Bind Mounts** (You specify exact location)
   ```bash
   -v /host/path:/container/path
   # Example: -v ~/repos/project:/app
   ```
   - Direct connection between host folder and container folder
   - Changes visible in BOTH locations immediately
   - Good for development (edit files on host, run in container)

**Key Understanding:**
- Volumes MUST be specified at `docker run` time
- Cannot add volumes to already-created containers
- Without volumes, databases lose all data when container stops
- Use `$(pwd)` for "current directory" in volume paths

#### 4. **Dockerfiles & Building Images**

**Created First Dockerfile:**
```dockerfile
FROM python:3.12-slim          # Start with base image
RUN pip install pandas pyarrow # Install dependencies
WORKDIR /app                   # Set working directory
COPY script.py script.py       # Copy files into image
ENTRYPOINT ["python", "script.py"]  # Default command
```

**Build Process:**
```bash
docker build -t my-pipeline:v1 .
# -t = tag/name the image
# . = look for Dockerfile in current directory
```

**Run with Arguments:**
```bash
docker run my-pipeline:v1 5
# The "5" gets passed as sys.argv[1] to the script
```

**Understanding Achieved:**
- Dockerfile instructions execute DURING build (creating image)
- ENTRYPOINT defines what runs when container starts
- Images are snapshots - build once, run anywhere
- This solves "works on my machine" problem

#### 5. **First Data Pipeline Built**

**Pipeline Components:**
```python
import sys
import pandas as pd

# Get command line argument
day = sys.argv[1]

# Create data
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Export to Parquet format
df.to_parquet(f'output_day_{day}.parquet')
```

**Key Concepts:**
- **sys.argv**: Command line arguments in Python
  - `sys.argv[0]` = script name
  - `sys.argv[1]` = first argument
- **Parquet**: Compressed columnar data format (efficient for big data)
- **Pipeline Pattern**: Input → Process → Output

**Successfully Containerized:**
- Runs in Docker container
- No Python installation needed on host
- Portable across any system with Docker

#### 6. **PostgreSQL in Docker**

**Database Container Setup:**
```bash
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:16
```

**Key Concepts Clarified:**

**Environment Variables (`-e`):**
- Configuration passed to program at startup
- PostgreSQL reads these to:
  - Create user account
  - Set password
  - Initialize database
- Like passing settings without editing code

**Port Mapping (`-p 5432:5432`):**
```
Host Computer                    Docker Container
localhost:5432  ←→  DOCKER  ←→  container:5432
     ↑                              ↑
  Your apps                   PostgreSQL server
  connect here               actually runs here
```
- Left number (5432) = port on YOUR computer
- Right number (5432) = port INSIDE container
- PostgreSQL default port is 5432
- Allows connections to `localhost:5432` to reach database in container

**Connection Tool: pgcli**
```bash
python -m uv add pgcli
python -m uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
# -h = host (localhost)
# -p = port (5432)
# -u = username (root)
# -d = database name (ny_taxi)
```

### 🔄 Currently Working On

**Data Ingestion (Chapter 5):**
- Downloading NYC taxi dataset (Parquet format)
- Loading real data into PostgreSQL using pandas
- Understanding data engineering workflow:
  1. Download data (CSV/Parquet)
  2. Transform with pandas
  3. Load into database (PostgreSQL)
  4. Query with SQL

**Last Known Issue:**
- Attempting to download dataset from URL
- Need to troubleshoot download errors

## Technical Terms Glossary

### Core Infrastructure
- **Container**: Isolated, lightweight environment that packages code + dependencies
- **Image**: Template/blueprint for creating containers (read-only)
- **Volume**: Persistent storage for containers (survives container deletion)
- **Host**: Your actual computer (outside Docker)
- **Port**: Communication endpoint for applications (like apartment numbers)
- **Localhost**: Your computer talking to itself (127.0.0.1)

### Docker Specific
- **Dockerfile**: Recipe/instructions to build a Docker image
- **ENTRYPOINT**: Command that runs when container starts
- **WORKDIR**: Default directory inside container
- **Base Image**: Starting point (e.g., `python:3.12-slim`)
- **Tag**: Version label for images (e.g., `my-image:v1`)
- **Daemon**: Background service (Docker Desktop runs Docker daemon)

### Development Tools
- **Virtual Environment (venv)**: Isolated Python environment for project
- **uv**: Modern Python package manager (faster than pip)
- **Git**: Version control system (tracks code changes)
- **Repository (repo)**: Folder tracked by Git
- **Commit**: Snapshot of code at a point in time
- **Bash**: Shell language for terminal commands
- **CLI (Command Line Interface)**: Text-based way to control computer

### Data Engineering
- **ETL**: Extract, Transform, Load (data pipeline pattern)
- **Parquet**: Columnar file format (compressed, efficient)
- **PostgreSQL**: Open-source relational database
- **SQL**: Language for querying databases
- **pgcli**: Terminal tool for PostgreSQL (like a fancy SQL prompt)
- **Pipeline**: Automated data processing workflow

## Key Realizations & Breakthroughs

### 1. "Works on My Machine" Problem
**Before Understanding:**
- Confusion about why code works on one computer but not another
- Frustration with dependency management

**After Understanding:**
- Docker containers package EVERYTHING needed
- Same container runs identically anywhere
- No more "but it works on my machine!"

### 2. Stateless vs Stateful
**Key Insight:**
- Containers are designed to be temporary and disposable
- Data MUST be saved outside container (volumes) to persist
- This design enables easy scaling and replication

### 3. Images vs Containers Analogy
**Mental Model:**
- Image = Cookie cutter (one template)
- Container = Cookie (many from one cutter)
- Each cookie is independent
- Breaking one cookie doesn't affect the cutter

### 4. Why Docker for Databases?
**Realization:**
- Installing PostgreSQL on Windows = complex, version conflicts
- Docker PostgreSQL = one command, clean, disposable
- Can run multiple database versions simultaneously
- Easy to reset/recreate without affecting system

### 5. Environment Variables Purpose
**Understanding:**
- NOT for storing code
- FOR: Configuration that changes per environment
- Examples: Database passwords, API keys, settings
- Keeps sensitive info out of code

## Common Mistakes & Lessons Learned

### Mistake 1: Using `--rm` Inappropriately
**What Happened:**
- Ran Ubuntu container with `--rm`
- Installed Python inside container
- Exited container
- Everything disappeared!

**Lesson:**
- `--rm` means "delete on exit"
- Use for temporary/testing only
- For permanent setups, use Dockerfile

### Mistake 2: Forgetting Volumes for Databases
**Risk:**
- Running PostgreSQL without `-v` flag
- All data lost when container stops

**Solution:**
- ALWAYS use named volumes for databases
- Data survives container deletion

### Mistake 3: Port Already in Use
**Problem:**
- Two containers trying to use same host port
- Error: "port is already allocated"

**Solution:**
- Check running containers: `docker ps`
- Stop conflicting container
- Or use different host port: `-p 5433:5432`

### Mistake 4: Docker Desktop Not Running
**Symptom:**
- "EOF" errors
- "Cannot connect to Docker daemon"

**Solution:**
- Check system tray for Docker whale icon
- Restart Docker Desktop
- Wait for "Engine running" status

### Mistake 5: Missing `/` in Paths
**Error:**
```bash
-v ~repos/project:/app  # WRONG (missing /)
-v ~/repos/project:/app # CORRECT
```

**Lesson:**
- `~` needs `/` after it
- Represents home directory path

## Your Learning Journey Patterns

### What Works Well For You:
1. **Visual Diagrams**: ASCII art diagrams help cement understanding
2. **Before/After Comparisons**: Seeing problems vs solutions
3. **Breaking Down Complexity**: Step-by-step explanations
4. **Hands-On Practice**: Learning by doing, not just reading
5. **Understanding "Why"**: Need context before diving into "how"
6. **Real Examples**: Concrete scenarios more helpful than abstract concepts

### Questions You Ask (Shows Deep Thinking):
- "Why can't we just...?" (exploring alternatives)
- "What if...?" (edge cases and scenarios)
- "What's the difference between X and Y?" (comparative learning)
- "Does it matter if...?" (understanding constraints)
- "Why is this designed this way?" (architectural reasoning)

### Your Strengths:
- Identifying gaps in understanding before moving forward
- Asking clarifying questions
- Building mental models
- Connecting concepts
- Documenting learning (exports, note-taking)

## What's Next in Your Learning Path

### Remaining Module 1 Topics:
1. **Data Ingestion Scripts** (Current focus)
   - Download NYC taxi data
   - Pandas DataFrame operations
   - Writing data to PostgreSQL
   
2. **pgAdmin** (Database GUI)
   - Visual database management
   - Running in Docker alongside PostgreSQL
   
3. **Docker Compose**
   - Running multiple containers together
   - Networking between containers
   - One command to start entire stack
   
4. **Terraform Basics**
   - Infrastructure as Code
   - Creating cloud resources (GCP)
   - `terraform init`, `plan`, `apply`, `destroy`

5. **Module 1 Homework**
   - Practical exercises
   - Testing understanding
   - Building portfolio projects

### Skills You'll Build:
- Multi-container applications
- Database operations at scale
- Cloud infrastructure provisioning
- Production-grade data pipelines

## Module 1 Key Takeaways (So Far)

1. **Docker solves the "works on my machine" problem** by containerizing applications
2. **Containers are disposable** - design for statelessness, persist data in volumes
3. **Dockerfiles are recipes** - write once, build anywhere, run everywhere
4. **Volumes enable persistence** - named volumes for databases, bind mounts for development
5. **Port mapping connects containers to host** - bridge between isolated container and your computer
6. **Environment variables configure containers** - flexible, secure way to pass settings
7. **Virtual environments isolate Python projects** - prevents dependency conflicts
8. **Git tracks changes** - version control is essential for collaboration and recovery

## Context for Continuing Learning

### Your Setup:
- **OS**: Windows 10/11
- **Terminal**: Git Bash (MINGW64)
- **Docker**: Docker Desktop
- **Python**: 3.12 with uv package manager
- **Code Editor**: Presumably VS Code
- **Project Structure**:
  ```
  ~/repos/de-zoomcamp-2026/
  ├── module-1/
  │   ├── pipeline/
  │   │   ├── script.py
  │   │   ├── Dockerfile
  │   │   └── .venv/
  │   ├── docker-test/
  │   └── postgres-docker/
  ```

### Active Docker Resources:
- Named volume: `ny_taxi_postgres_data` (PostgreSQL data)
- Images pulled: `python:3.12-slim`, `python:3.9-slim`, `postgres:16`, `ubuntu`
- Built images: `my-pipeline:v1`

### Immediate Next Steps When Resuming:
1. Check if PostgreSQL container is running: `docker ps`
2. Navigate to module-1 directory: `cd ~/repos/de-zoomcamp-2026/module-1`
3. Continue with data ingestion chapter (downloading NYC taxi dataset)
4. Goal: Load real data into PostgreSQL and practice SQL queries

## Questions to Explore When Ready

These arose during learning but weren't fully answered:
1. Docker Compose networking details (how containers communicate)
2. Difference between Docker and Docker Desktop
3. How Docker storage actually works under the hood
4. Best practices for Dockerfile optimization (layer caching, image size)
5. When to use `CMD` vs `ENTRYPOINT`
6. Understanding Docker networks in detail
7. Security considerations (not running as root)
8. Multi-stage Docker builds

## Your Learning Philosophy

Based on this journey, you approach learning with:
- **Curiosity**: Want to understand underlying mechanisms
- **Thoroughness**: Not satisfied with surface-level knowledge
- **Practical Focus**: Learn by building, not just reading
- **Documentation**: Value of keeping records and notes
- **Patience**: Willing to slow down for deep understanding
- **Persistence**: Work through errors methodically

This context should help you (or future Claude conversations) pick up exactly where you left off with full understanding of your learning journey.
