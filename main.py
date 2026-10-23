import os
import requests
import subprocess
import webview as w
import sys
import ctypes
from tkinter import messagebox as msg
import webbrowser
dir = os.path.dirname(os.path.abspath(__file__))

def resolve_dns_via_doh(domain):
    """Resolves domain using Google's DNS-over-HTTPS API to bypass local ISP DNS blocks."""
    try:
        url = f"https://dns.google{domain}&type=A"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if "Answer" in data:
                return data["Answer"][0]["data"]
    except Exception as e:
        print(f"[-] DoH Resolution failed: {e}")
    return None

def download_roblox_file(name, filename):
    full_path = os.path.join(dir, filename)
    domain = "setup.rbxcdn.com"
    
    print(f"Resolving IP for {domain}...")
    ip = resolve_dns_via_doh(domain)
    
    if ip:
        # If successfully resolved, we bypass local DNS issues by calling IP directly
        # while passing the correct Host header so Cloudflare routes it correctly.
        download_url = f"https://{ip}/{filename}"
        print(f"Downloading {name} from secure bridge {download_url}...")
    else:
        # Fallback to standard URL if DoH fails
        download_url = f"https://{domain}/{filename}"
        print(f"Downloading {name} from standard URL...")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Host": domain
        }
        
        # verify=False prevents SSL handshake errors due to the IP mismatch with the cert
        with requests.get(download_url, headers=headers, stream=True, timeout=25, verify=False) as response:
            response.raise_for_status()

            # Ensure we are actually downloading a binary file, not a block page HTML text
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' in content_type:
                raise Exception("The server returned an HTML error page instead of the executable binary.")

            with open(full_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        print(f"Success! File saved. Running: {full_path}\n")
        subprocess.Popen([full_path], shell=True) 
        return True
    except Exception as e:
        print(f"Error while downloading {name}: {e}\n")
        msg.showerror("NecoBlox Error", f"Failed to download {name}:\n{e}")
        return False

class api:
    def run(self):
        installer_path = os.path.join(dir, "RobloxPlayerInstaller.exe")
        if not os.path.exists(installer_path):
            download_roblox_file("Roblox Player", "RobloxPlayerInstaller.exe")
        else:
            subprocess.Popen([installer_path], shell=True)

    def runstudio(self):
        studio_path = os.path.join(dir, "RobloxStudioLauncherBeta.exe")
        if not os.path.exists(studio_path):
            download_roblox_file("Roblox Studio", "RobloxStudioLauncherBeta.exe")
        else:
            subprocess.Popen([studio_path], shell=True)
    def rerun(self):
            installer_path = os.path.join(dir, "RobloxInstaller.exe")
            if not os.path.exists(installer_path):
                            download_roblox_file("Roblox Player", "RobloxStudioLauncherBeta.exe")
                            msg.showinfo("NecoBlox", "ReInstalled!")
            else:
                            os.system("del RobloxInstaller.exe")
                            download_roblox_file("Roblox Player", "RobloxStudioLauncherBeta.exe")
                            msg.showinfo("NecoBlox", "ReInstalled!")
    def restudio(self):
            studio_path = os.path.join(dir, "RobloxStudioLauncherBeta.exe")
            if not os.path.exists(studio_path):
                download_roblox_file("Roblox Studio", "RobloxStudioLauncherBeta.exe")
            else:
                os.system("del RobloxStudioLauncherBeta.exe")
                download_roblox_file("Roblox Studio", "RobloxStudioLauncherBeta.exe")
                subprocess.Popen([studio_path], shell=True)

    def fixicons(self):
        print("[*] Starting hosts file patch...")
        
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            is_admin = False
            
        if not is_admin:
            msg.showwarning("NecoBlox Warning", "Please run the application as Administrator to apply this fix!")
            return False

        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        if not os.path.exists(hosts_path):
            print("[-] Error: Hosts file not found.")
            return False

        roblox_domains = [
            ("127.0.0.1", "roblox.com"),
            ("127.0.0.1", "www.roblox.com"),
            ("127.0.0.1", "assetgame.roblox.com")
        ]

        with open(hosts_path, "r", encoding="utf-8") as file:
            current_content = file.read()

        lines_to_write = []
        for ip, domain in roblox_domains:
            entry = f"{ip} {domain}"
            if domain not in current_content:
                lines_to_write.append(entry)

        if not lines_to_write:
            msg.showinfo("NecoBlox", "All entries are already present in the hosts file!")
            return True

        try:
            with open(hosts_path, "a", encoding="utf-8") as file:
                file.write("\n")
                for line in lines_to_write:
                    file.write(f"{line}\n")
            msg.showinfo("NecoBlox", "Hosts file updated successfully!")
            return True
        except Exception as e:
            msg.showerror("NecoBlox Error", f"Error writing to hosts file: {e}")
            return False
    def github(self):
         webbrowser.open_new_tab("https://github.com/Cat-NS/NecoBlox")
class main:
    print("Running!")
    index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    index_url = f"file:///{index_path.replace(os.sep, '/')}"
    w.create_window("NecoBlox V3.0", url=index_url, js_api=api())
    w.start()
