#!/usr/bin/env bash
set -euo pipefail

echo "==> Compiling lzss..."
gcc lib/lzss/lzss.c -o lib/lzss/lzss -O3

echo "==> Installing dependencies..."
uv sync --all-extras --dev

echo "==> Running PyInstaller..."
uv run pyinstaller VW_Flash_GUI_mac.spec --noconfirm

echo "==> Creating DMG..."
DMG_NAME="VW_Flash_GUI.dmg"
APP_PATH="dist/VW_Flash_GUI.app"

if [ ! -d "$APP_PATH" ]; then
    echo "ERROR: $APP_PATH not found. PyInstaller build may have failed."
    exit 1
fi

# Remove old DMG if present
rm -f "dist/$DMG_NAME"

hdiutil create \
    -volname "VW Flash GUI" \
    -srcfolder "$APP_PATH" \
    -ov \
    -format UDZO \
    "dist/$DMG_NAME"

echo "==> Done! DMG created at dist/$DMG_NAME"
