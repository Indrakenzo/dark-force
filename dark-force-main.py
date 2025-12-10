import time
import random
import sys
import string

# Definisi Warna (Wajib biar hacker banget)
HIJAU = "\033[92m"
MERAH = "\033[91m"
PUTIH = "\033[97m"
KUNING = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear_screen():
    # Simulasi clear screen simple pake print enter banyak
    print("\n" * 50)

def banner():
    print(CYAN + "=" * 60)
    print("      MULTI-PLATFORM BRUTE FORCE TOOL - V.3.5 (ROOT)      ")
    print("      Created by: Unknown Cyber Team                      ")
    print("      Access: GRANTED | Encryption: 256-bit               ")
    print("=" * 60 + RESET)

def loading_bar(durasi, pesan):
    sys.stdout.write(PUTIH + f"[*] {pesan} [")
    sys.stdout.flush()
    for _ in range(20):
        time.sleep(durasi / 20)
        sys.stdout.write(HIJAU + "#")
        sys.stdout.flush()
    sys.stdout.write(PUTIH + "] DONE\n" + RESET)

def generate_fake_password():
    # Bikin password yang kelihatan susah/complex
    chars = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choice(chars) for _ in range(random.randint(8, 14)))

def main():
    clear_screen()
    banner()
    
    # Input Username Target
    target_user = input(KUNING + "\n[?] Masukkan Username Target (tanpa @): " + RESET)
    if not target_user:
        print(MERAH + "[!] Username tidak boleh kosong!" + RESET)
        sys.exit()

    # Menu Pilihan Platform
    print(PUTIH + "\n[+] Pilih Platform Target Serangan:" + RESET)
    print(" 1. Facebook (Meta)")
    print(" 2. Instagram")
    print(" 3. X (Twitter)")
    print(" 4. Threads")
    print(" 5. TikTok (Bonus)")
    
    pilihan = input(KUNING + "\n[?] Masukkan nomor [1-5]: " + RESET)
    
    platforms = {
        "1": "Facebook",
        "2": "Instagram",
        "3": "X (Twitter)",
        "4": "Threads",
        "5": "TikTok"
    }
    
    platform_name = platforms.get(pilihan, "Unknown Server")
    
    print(f"\n{HIJAU}[+] Target Locked: {target_user} on {platform_name}{RESET}")
    time.sleep(1)
    
    # Drama Hacking Dimulai
    loading_bar(3, "Connecting to database")
    loading_bar(2, "Bypassing 2FA Security")
    loading_bar(4, "Injecting SQL Payload")
    
    print(f"\n{KUNING}[!] STARTING DICTIONARY ATTACK...{RESET}")
    time.sleep(1)

    # Fake Brute Force Loop (Visual Matrix)
    try:
        # Loop ini cuma buat gaya-gayaan
        for i in range(150): 
            fake_pass = generate_fake_password()
            print(MERAH + f"[-] Trying: {fake_pass} ... ACCESS DENIED" + RESET)
            time.sleep(0.02) # Kecepatan scroll

            # Sesekali pause biar kayak lagi mikir
            if random.random() < 0.05:
                time.sleep(0.5)
                print(CYAN + "[*] Switching Proxy..." + RESET)

        # HASIL AKHIR (PRANK)
        print("\n" + HIJAU + "=" * 60)
        print(f"    [SUCCESS] PASSWORD HASH CRACKED FOR: {target_user}")
        print("=" * 60 + RESET)
        print(PUTIH + f"[!] System detected multiple possible passwords.")
        print(f"[!] Probability Accuracy: 98.9%")
        print(f"[!] Menampilkan 20 kemungkinan password teratas:\n" + RESET)
        
        time.sleep(2)
        
        print(CYAN + "+----+------------------+-------------+")
        print(f"| ID | PASSWORD CANDIDATE | PROBABILITY |")
        print("+----+------------------+-------------+" + RESET)
        
        # Generate 20 password palsu yang susah
        for i in range(1, 21):
            fake_result = generate_fake_password()
            prob = random.randint(75, 99)
            print(f"| {i:02d} | {fake_result:<16} | {prob}%         |")
            time.sleep(0.1) # Muncul satu-satu biar dramatis
            
        print(CYAN + "+----+------------------+-------------+" + RESET)
        
        print(KUNING + "\n[TIPS] Silakan coba password di atas satu per satu.")
        print("[NOTE] Jangan lupa gunakan VPN saat login!" + RESET)
        print(HIJAU + "\n[+] Session Closed. Happy Hacking!" + RESET)

    except KeyboardInterrupt:
        print(MERAH + "\n[!] Operation cancelled by user." + RESET)

if __name__ == "__main__":
    main()
