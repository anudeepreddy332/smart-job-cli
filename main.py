import argparse

def main():
    parser = argparse.ArgumentParser(description="Job Scraper CLI")

    parser.add_argument('--keyword',type=str, required=True,
                        help='Job keyword to search for (e.g. Python Developer)')
    parser.add_argument('--location',type=str,
                        help='Job location (e.g. Hyderabad)')
    parser.add_argument('--remote',action='store_true',
                        help='Include only remote jobs')
    parser.add_argument('--min-salary',type=int,
                        help='minimum salary filter')
    parser.add_argument('--output',type=str,default='jobs.csv',help='Output CSV file name')

    args = parser.parse_args()

    print(f"Keyword: {args.keyword}")
    print(f"Location: {args.location}")
    print(f"Remote: {args.remote}")
    print(f"Min Salary: {args.min_salary}")
    print(f"Output File: {args.output}")

if __name__ == "__main__":
    main()