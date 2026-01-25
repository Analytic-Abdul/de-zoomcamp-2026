# Module 1: Technical Glossary

A plain-English guide to technical terms in software engineering and Docker.

---

## General Computer Basics

| Term | Explanation |
|------|-------------|
| **Operating System (OS)** | The "brain" software of your computer that manages everything (Windows, macOS, Linux). |
| **Kernel** | The heart of the OS that talks directly to your computer's hardware. |
| **File System** | How your computer organizes and stores files and folders. |
| **Root** | The absolute starting point of your file system. On Windows: `C:\` |
| **Home Folder** | Your personal folder: `C:\Users\YourName`. The `~` symbol is a shortcut to this. |
| **Terminal / Command Line** | A window where you type text commands instead of clicking icons. |
| **Bash** | A "language" used in the terminal. Git Bash brings it to Windows. |
| **.bashrc** | Settings file your terminal reads on startup. Like "house rules." |
| **Localhost** | A nickname your computer uses to talk to itself (not the internet). |
| **Ports** | Like apartment numbers. Each program listens on a specific port (e.g., 5432 for PostgreSQL). |

---

## Command Line Navigation and Commands

| Command | What It Does |
|---------|--------------|
| `pwd` | Print Working Directory - shows where you are |
| `ls` | List files and folders in current directory |
| `cd foldername` | Go INTO a folder |
| `cd ..` | Go UP one folder (parent) |
| `cd ~` | Go to your HOME folder |
| `cd /` | Go to ROOT (very top) |
| `mkdir name` | Create a new folder |
| `mv` | Move or rename |
| `rm` | Delete |
| ` git init  ` | Start tracking a folder |
| ` git add . ` | Stage changes |
| ` git commit -m "commit message" ` | Save checkpoint (Commit changes) |
| ` git push  ` | Upload changes to Github |
| ` git pull  ` | Download changes from Github |

---

## Coding and Data Tools

| Term | Explanation |
|------|-------------|
| **VS Code** | A powerful text editor for programmers. |
| **Python** | A beginner-friendly programming language popular in data engineering. |
| **Dependencies / Libraries** | Pre-built toolkits (e.g., Pandas for data tables). |
| **Virtual Environment (venv)** | An isolated "bubble" for your project's dependencies. |
| **Database (PostgreSQL)** | A system to store and quickly retrieve massive amounts of data. |
| **CSV** | Comma-Separated Values. Simple text format for tables. |
| **Parquet** | Compressed, optimized format for big data. Much faster than CSV. |
| **CLI** | Command Line Interface. Tools you use by typing commands. |
| **API** | How programs talk to each other - like a waiter between you and the kitchen. |

---

## Git and GitHub

| Term | Explanation |
|------|-------------|
| **Git** | Tracks every change to your code, like save points in a video game. |
| **Repository (Repo)** | A folder tracked by Git with its entire change history. |
| **Local Repo** | The repo on YOUR computer. |
| **Remote Repo** | The repo on GitHub (in the cloud). |
| **origin** | A nickname for your GitHub repo's URL. |
| **Clone** | Download a copy of someone's repo to your computer. |
| **Commit** | A "save point" with a message describing what changed. |
| **Push** | Send your local commits UP to GitHub. |
| **Pull** | Bring GitHub's changes DOWN to your computer. |
| **Fetch** | Check what's new on GitHub without merging it yet. |
| **Branch** | A parallel version of your code. `main` is the primary branch. |

---

## Docker Jargon

| Term | Explanation |
|------|-------------|
| **Docker** | Packages an application and dependencies into a portable container. |
| **Image** | A "recipe" or "blueprint" - saved snapshot, not running yet. |
| **Container** | A running instance of an image. An isolated box where your app lives. |
| **Dockerfile** | Text file with instructions to build a Docker image. |
| **Docker Compose** | Runs multiple containers together using one YAML file. Lives on HOST, not in containers. |
| **Docker Hub** | An "app store" for Docker images. |
| **Docker Daemon** | The background engine that builds and runs containers. |
| **Isolated** | What happens in a container stays there. Your computer is safe. |
| **Stateless** | Containers are "forgetful" - data lost when removed (unless you use volumes). |
| **Volume** | A tunnel connecting your computer's folder to the container's folder. Persists data. |
| **Port Mapping (-p)** | Connecting your port to a container's port. `-p 8080:80` |
| **Environment Variables (-e)** | Config values passed into a container (passwords, settings). |
| **Base Image** | The starting point you build on (e.g., `python:3.9`). |
| **Tag** | A version label for images (e.g., `python:3.9` vs `python:3.11`). |
| **Layers** | Images are built in stacked layers. Unchanged layers are cached. |
| **Entry Point** | The first command that runs when a container starts. |
| **Docker Network** | Private connection letting containers talk to each other by name. |

---

## Cloud & Infrastructure

| Term | Explanation |
|------|-------------|
| **Cloud** | Other people's computers you rent over the internet. |
| **Virtual Machine (VM)** | A "pretend" computer inside a real computer. Heavier than containers. |
| **GCP** | Google Cloud Platform. Google's cloud services. |
| **Infrastructure as Code (IaC)** | Write code to create cloud resources instead of clicking. |
| **Terraform** | A tool for IaC. Write `.tf` files to create cloud resources. |
| **Provisioning** | Setting up resources (servers, databases) for use. |
| **Service Account** | A "robot user" for your code to access cloud services. |
| **Bucket** | Cloud storage for files. Like an unlimited folder in the cloud. |

---

## Data Engineering

| Term | Explanation |
|------|-------------|
| **Pipeline** | Steps data flows through. Raw data in, clean data out. |
| **ETL** | Extract, Transform, Load - the classic data pipeline pattern. |
| **Schema** | Blueprint of a database table: column names and data types. |
| **Ingestion** | Pulling data into your system from external sources. |
| **Batch Processing** | Processing large chunks of data on a schedule. |
| **Streaming** | Processing data immediately as it arrives. |
