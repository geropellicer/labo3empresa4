#!/bin/bash

# Exit in case of error
set -e

# Extract the current version
echo "Extracting current version..."
current_version=$(grep -Po "(?<=version=\')[^\']+|(?<=version=\")[^\"]+" setup.py)
echo "Current version is $current_version"

# Increment the version or set a new one
echo "Calculating new version..."
IFS='.' read -ra VERSION <<< "$current_version"
if [ ${#VERSION[@]} -ne 3 ]; then
    echo "Error: Current version is not in the format X.Y.Z"
    exit 1
fi

VERSION[2]=$((VERSION[2]+1))
new_version="${VERSION[0]}.${VERSION[1]}.${VERSION[2]}"
echo "New version is $new_version"

# Update setup.py with the new version
echo "Updating setup.py with the new version..."
sed -i "s/version='$current_version'/version='$new_version'/" setup.py

# Continue with your build and publish process
echo "Building and publishing new version..."

# Remove previous build artifacts
echo "Cleaning up old build artifacts..."
rm -rf build/ dist/ *.egg-info

# Build the package
echo "Building Source and Wheel (universal) distribution..."
python setup.py sdist bdist_wheel

# Upload the package to PyPI using Twine
echo "Uploading the package to PyPI via Twine..."
twine upload --repository empresa4 dist/*

echo "Publishing process finished successfully!"
