import subprocess

def run_sqlmap(url):
    """
    Run sqlmap on a target URL.
    """
    print(f"[*] Testing URL with sqlmap: {url}")
    try:
        command = [
            "sqlmap",
            "-u", url,
            "--batch",
            "--level", "3",
            "--risk", "3",
            "--dbs"
        ]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] sqlmap encountered an error: {e}")
    except Exception as e:
        print(f"[-] Error running sqlmap: {e}")