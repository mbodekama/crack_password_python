import hashlib
mots_hacking = [
     "piratage", "cryptographie", "malware", "phishing",
    "firewall", "exploit", "proxy", "botnet", "backdoor",
    "bruteforce", "ransomware", "cheval_de_Troie", "keylogger", "honeypot",
    "spoofing", "VPN", "DNS", "trojan", "intrusion"
]

file = open('extrait_bd_pirate.txt', 'a')
for mot in mots_hacking:
    mot_hash = hashlib.md5(mot.encode()).hexdigest()
    file.write(mot_hash+"\n")
file.close()


