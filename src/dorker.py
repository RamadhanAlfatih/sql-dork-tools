from googlesearch import search

def perform_dorking(query, num_results=10):
    """
    Perform Google Dorking to find URLs.
    """
    urls = []
    try:
        print(f"[*] Performing Google Dorking for: {query}")
        for url in search(query, num=num_results, stop=num_results, pause=2):
            print(f"[+] Found URL: {url}")
            urls.append(url)
    except Exception as e:
        print(f"[-] Error during Google Dorking: {e}")
    return urls