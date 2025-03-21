import argparse
from src.dorker import perform_dorking
from src.sqlmapper import run_sqlmap

def main():
    parser = argparse.ArgumentParser(description="Automated Google Dorking and SQL Injection Testing Tool")
    parser.add_argument("-q", "--query", required=True, help="Google Dork query")
    parser.add_argument("-n", "--num_results", type=int, default=5, help="Number of results to fetch")
    args = parser.parse_args()

    # Perform Google Dorking
    urls = perform_dorking(args.query, args.num_results)

    # Test each URL with sqlmap
    for url in urls:
        run_sqlmap(url)

if __name__ == "__main__":
    main()