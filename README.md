# 🔍 Smart Job CLI
A simple command-line tool that searches job listings on Google using SerpAPI and saves them to a CSV.

## 🚀 Features
- Search by keyword and location
- Pull up to 50 job listings
- Extracts job title, company, location, and URL
- Outputs to CSV

## 🛠️ CLI Options
| Option     | Description                                  | Required |
|------------|----------------------------------------------|----------|
| --keyword  | Job title or role to search (e.g. "DevOps")  | Yes      |
| --location | Job location (e.g. "Bangalore")              | Yes      |
| --limit    | Number of listings to pull (default: 10)     | No       |
| --output   | CSV output file (default: jobs.csv)          | No       |

## 📦 Requirements
• Python 3.7+
• requests, pandas, python-dotenv
• SerpAPI account + .env file with:
	SERP_API=your_api_key_here

## 📁 Project Structure
	smart_job_cli/
	├── main.py         # CLI entrypoint
	├── scraper.py      # Scraping logic
	├── utils.py        # CSV handling
	├── .env            # Your SerpAPI key (gitignored)
	├── .gitignore
	├── jobs.csv        # Output file (gitignored)

## 🧠 Example Usage
```bash
python main.py --keyword "Python Developer" --location "Hyderabad" --limit 50
