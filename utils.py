import pandas as pd

def save_to_csv(jobs, filename):
    if not jobs:
        print("[WARN] No jobs to save.")
        return

    df = pd.DataFrame(jobs, columns=["title", "company", "location", "url"])
    df.to_csv(filename, index=False)
    print(f"[INFO] Saved {len(df)} jobs to {filename}")