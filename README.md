# Smart Job CLI 🔍💼

A command-line tool to scrape job postings based on keyword, location, remote preferences, and salary filter.

## 📦 Features
  - Accepts job search criteria from the command line
  - Filters by keyword, location, remote jobs, and minimum salary
  - (Coming soon) Scrapes jobs and saves to CSV

🛠️ Coming Soon
	•	Live scraping from Indeed or other job sites
	•	Salary filtering logic
	•	Pagination handling
	•	Error handling and retry logic

🧠 Built With
	•	Python 3.13
	•	argparse (CLI argument parsing)

## 🚀 Usage
```bash
python main.py --keyword "Python Developer" --location "Delhi" --remote --min-salary 80000 --output jobs.csv
