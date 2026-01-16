# Docker Architecture: How It All Fits Together

## The Big Picture

```
YOUR COMPUTER (Host Machine)
│
├── your-project/
│   ├── docker-compose.yml    ← ONE file, lives HERE (not in containers)
│   │
│   ├── app/
│   │   ├── Dockerfile        ← Recipe for the Python app
│   │   └── main.py
│   │
│   └── database/
│       └── (uses pre-built postgres image, no Dockerfile needed)
│
└── Docker Engine (daemon running in background)
    │
    ├── Container 1: Python App    ← Created from app/Dockerfile
    │   (isolated box)
    │
    └── Container 2: PostgreSQL    ← Created from postgres image
        (isolated box)

    ↕ Containers talk via Docker Network
```

---

## Key Insight: Where Does docker-compose.yml Live?

**WRONG thinking:** "Each container has a docker-compose file"

**CORRECT:** There's only ONE docker-compose.yml, and it lives on your computer (the host), not inside any container.

### Analogy

| Concept | Analogy |
|---------|---------|
| **docker-compose.yml** | Orchestra conductor's sheet music - ONE person directing everyone |
| **Containers** | Musicians - they don't have the conductor's notes, they just play |
| **Docker Network** | The stage they all perform on together |

---

## The Flow When You Run `docker-compose up`

```
1. You run: docker-compose up

2. Docker reads the ONE docker-compose.yml file

3. It builds/pulls all the images needed

4. It creates containers from those images

5. It creates a network so containers can talk

6. It starts all containers together
```

---

## Example docker-compose.yml

```yaml
version: '3.8'

services:
  # Container 1
  python-app:
    build: ./app              # Build from Dockerfile in ./app folder
    ports:
      - "8080:8080"           # My port 8080 → container's 8080
    depends_on:
      - database              # Start database first

  # Container 2
  database:
    image: postgres:13        # Use pre-built image from Docker Hub
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - ./data:/var/lib/postgresql/data   # Save data to my computer
```

**One file. Controls everything. Lives on your machine, not in containers.**

---

## Image vs Container

```
┌─────────────────┐
│     IMAGE       │  ← Blueprint/Recipe (not running)
│  (frozen file)  │
└────────┬────────┘
         │
         │  docker run
         ▼
┌─────────────────┐
│   CONTAINER     │  ← Running instance (alive)
│  (isolated box) │
└─────────────────┘
```

One image can create MANY containers (like one recipe can make many cakes).

---

## The Host vs Container Relationship

```
┌─────────────────────────────────────────────────┐
│  HOST MACHINE (Your Computer)                   │
│                                                 │
│   ┌─────────────┐      ┌─────────────┐         │
│   │ Container A │      │ Container B │         │
│   │             │      │             │         │
│   │  Port 5000  │      │  Port 5432  │         │
│   └──────┬──────┘      └──────┬──────┘         │
│          │                    │                 │
│          └────────┬───────────┘                 │
│                   │                             │
│            Docker Network                       │
│                   │                             │
└───────────────────┼─────────────────────────────┘
                    │
              Port Mapping
                    │
                    ▼
            Outside World
         (your browser, etc.)
```

---

## Common Docker Commands

| Command | What It Does |
|---------|--------------|
| `docker build -t myapp .` | Build an image from Dockerfile in current folder |
| `docker run myapp` | Create and start a container from an image |
| `docker ps` | List running containers |
| `docker ps -a` | List ALL containers (including stopped) |
| `docker images` | List all images on your machine |
| `docker stop <id>` | Stop a running container |
| `docker rm <id>` | Remove a stopped container |
| `docker rmi <image>` | Remove an image |
| `docker-compose up` | Start all services defined in docker-compose.yml |
| `docker-compose down` | Stop and remove all containers from compose |
| `docker-compose up -d` | Start in "detached" mode (background) |
| `docker logs <id>` | View output/logs from a container |
| `docker exec -it <id> bash` | "SSH into" a running container |
