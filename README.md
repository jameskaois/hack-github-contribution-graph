# Hack GitHub Contribution Graph 📊
This repository contains a simple bash script to **backdate your GitHub contributions**. It's not magic, just a straightforward way to create commits in the past, helping you fill out your contribution graph for specific dates.

## How It Works 💻
The script automates the process of creating commits in a specified date range. It reads dates from a `date.txt` file, creates a commit for each date using the `git commit --date` command, and then pushes these changes to your GitHub repository. This allows Git to record the commit as if it happened on that past date.

## What You Can Create ✨
This script gives you control over your past contribution history on GitHub. Here are a couple of ways you can utilize it:

### Fill Missed Contributions 🗓️
You can easily fill in days where you might have forgotten to commit or had a gap in your activity. This helps in maintaining a consistent-looking contribution graph.

### Draw Patterns on Your Graph 🎨
Beyond just filling in gaps, with careful planning of your `date.txt` file, you can even "draw" patterns or shapes on your contribution graph by strategically placing commits on specific dates.

## Setup ⚙️
Before you begin, make sure you have:
- Git installed on your system.
- A GitHub repository (this script assumes it's linked as `origin`).

`date.txt` Format 📅
Create a file named `date.txt` in the root of your repository. Each line in this file should contain a single date in the `YYYY-MM-DD` format.

Example `date.txt`:
```
2023-01-01
2023-01-02
2023-01-03
```

## Usage ▶️
1. **Init Git** locally and **add origin** to your repository:
```
git init
git remote add origin <your repo url>
```
2. **Create or update** `date.txt` with the dates you want to backdate contributions for, as described above.

3. **Make sure the** `contribution.txt` **file exists** in your repository, or it will be created.

4. **Copy the content** of [`hack-github-contribution.sh`](./hack-github-contribution.sh) file (from this repository) to your local `.sh` file.

5. **Run the script:**
```
bash your_script_name.sh
```
(Replace `your_script_name.sh` with the actual name of your `.sh` file, like `hack-github-contribution.sh`.)

The script will iterate through each date in `date.txt`, make a commit, and push it. After a date is successfully processed and pushed, it will be **removed from** `date.txt` to avoid re-processing on subsequent runs. If a push fails, the date will remain in `date.txt` for retries.

## Important Notes ⚠️
- **GitHub Contribution Graph Delay:** Even after successfully pushing backdated commits, it can take some time (usually a few minutes to **up to 24 hours**) for your GitHub profile's contribution graph to update. GitHub's graph is cached and not always real-time. Make sure the email address used in your Git commits is associated with your GitHub account.

## Disclaimer ✨
This tool is a **simple demonstration** of how Git commit dates and author information can be manipulated. It's not a "fancy" hacking tool, but rather leverages the basic functionalities of Git. It helps you understand that what you see on a contribution graph is based on commit metadata, which can be controlled.