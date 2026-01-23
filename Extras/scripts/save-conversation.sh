#!/bin/bash

# Save Conversation Script
# Moves exported Claude conversation to the correct module folder

# Usage: ./save-conversation.sh [module-number]
# Example: ./save-conversation.sh 1

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get module number from argument, default to 1
MODULE=${1:-1}
MODULE_FOLDER="module-$MODULE"

# Paths
HOME_DIR=~
REPO_DIR=~/repos/de-zoomcamp-2026
TARGET_DIR="$REPO_DIR/$MODULE_FOLDER"

# Find the most recent conversation file in home directory
CONV_FILE=$(ls -t "$HOME_DIR"/*.txt 2>/dev/null | head -1)

if [ -z "$CONV_FILE" ]; then
    echo -e "${RED}No .txt files found in home directory${NC}"
    exit 1
fi

# Get just the filename
FILENAME=$(basename "$CONV_FILE")

# Check if target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}Module folder doesn't exist: $TARGET_DIR${NC}"
    echo "Creating it..."
    mkdir -p "$TARGET_DIR"
fi

# Generate timestamp for unique naming
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
NEW_NAME="conversation-$TIMESTAMP.txt"

# Move and rename
mv "$CONV_FILE" "$TARGET_DIR/$NEW_NAME"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Conversation saved!${NC}"
    echo "  From: $CONV_FILE"
    echo "  To:   $TARGET_DIR/$NEW_NAME"
else
    echo -e "${RED}Failed to move file${NC}"
    exit 1
fi
