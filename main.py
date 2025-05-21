import argparse
from scraper import build_url, fetch_jobs
from utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Job Scraper CLI")

    parser.add_argument('--keyword',type=str, required=True,
                        help='Job keyword to search for (e.g. Python Developer)')
    parser.add_argument('--location',type=str,default='',
                        help='Job location (e.g. Hyderabad)')
    parser.add_argument('--limit',type=int,default=50,
                        help='Number of jobs to fetch (Max 100).')
    parser.add_argument('--output',type=str,default='jobs.csv',help='Output CSV file name')

    args = parser.parse_args()

    params = build_url(args.keyword, args.location)
    print(f"[INFO] Searching: {args.keyword} in {args.location or 'Anywhere'}")

    jobs = fetch_jobs(params,total_results=args.limit)
    print(f"[INFO] Found {len(jobs)} jobs")

    save_to_csv(jobs, args.output)

if __name__ == "__main__":
    main()