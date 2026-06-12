#!/bin/bash
# Build script for the Vibe Coding Builders Hackathon Guide PDF
# Generates cover page and content pages, then merges into final PDF

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}=== Vibe Coding Builders Hackathon Guide - Build Script ===${NC}"

# Check for required tools
echo -e "${YELLOW}Checking dependencies...${NC}"

if ! command -v node &> /dev/null; then
    echo -e "${RED}Error: Node.js is required but not installed.${NC}"
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
    exit 1
fi

# Check for PDF skill scripts
PDF_SKILL_DIR="${PDF_SKILL_DIR:-}"
if [ -z "$PDF_SKILL_DIR" ]; then
    echo -e "${YELLOW}Warning: PDF_SKILL_DIR not set. Attempting auto-detection...${NC}"
    if [ -d "$HOME/.skills/pdf" ]; then
        PDF_SKILL_DIR="$HOME/.skills/pdf"
    elif [ -d "/home/z/my-project/skills/pdf" ]; then
        PDF_SKILL_DIR="/home/z/my-project/skills/pdf"
    else
        echo -e "${RED}Error: Cannot find PDF skill directory. Set PDF_SKILL_DIR environment variable.${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}Using PDF skill: $PDF_SKILL_DIR${NC}"

# Step 1: Generate cover page PDF
echo -e "${YELLOW}Step 1/3: Generating cover page...${NC}"
node "$PDF_SKILL_DIR/scripts/html2poster.js" \
    "$PROJECT_DIR/cover.html" \
    --output "$PROJECT_DIR/cover.pdf" \
    --width 210mm

# Step 2: Generate content PDF
echo -e "${YELLOW}Step 2/3: Generating content pages...${NC}"
node "$PDF_SKILL_DIR/scripts/html2pdf-next.js" \
    "$PROJECT_DIR/guide.html" \
    --output "$PROJECT_DIR/content.pdf" \
    --width 210mm \
    --height 297mm

# Step 3: Merge cover and content
echo -e "${YELLOW}Step 3/3: Merging PDFs...${NC}"
python3 "$PDF_SKILL_DIR/scripts/pdf.py" pages.merge \
    "$PROJECT_DIR/cover.pdf" \
    "$PROJECT_DIR/content.pdf" \
    -o "$PROJECT_DIR/hackathon-ideas-guide.pdf"

# Add metadata
python3 "$PDF_SKILL_DIR/scripts/pdf.py" meta.brand \
    "$PROJECT_DIR/hackathon-ideas-guide.pdf"

# Clean up temporary files
rm -f "$PROJECT_DIR/cover.pdf" "$PROJECT_DIR/content.pdf"

echo -e "${GREEN}=== Build Complete ===${NC}"
echo -e "${GREEN}Output: $PROJECT_DIR/hackathon-ideas-guide.pdf${NC}"
ls -lh "$PROJECT_DIR/hackathon-ideas-guide.pdf"
