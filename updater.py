import requests, utilities, subprocess, sys, os, time

base_url = "https://raw.githubusercontent.com/Zanzibarr/Telegram_Python_Notifier/main/"
version_control = "change_log.md"
update_setup_file = "update_setup.py"

down_folder = f"{utilities.base_path}/Downloads"


# --- LOGGING OPTIONS ---

if len(sys.argv) == 2 and sys.argv[1] not in ("d", "s", "ds"):
    print("Wrong arguments.")
    exit(1)
log_to_file = len(sys.argv) == 2 and "s" in sys.argv[1]


# --- VERSION CONTROL ---

r = requests.get(f"{base_url}{version_control}")

if not r.ok:
    print(f"Request to {base_url}{version_control} had response {r}")
    print(f"Exception: {r}")
    exit(1)

text = r.text

update = True
dev = len(sys.argv) == 2 and "d" in sys.argv[1]
newer = text.partition("Version ")[2].partition("\n")[0]

if not dev:
    o_v, o_p = utilities.version.partition(": ")[2].split(".")[:2]
    n_v, n_p = newer.split(".")[:2]
    update = o_v+o_p != n_v+n_p

if not update:
    print("notify is already up-to-date.")
    exit(0)


# --- DOWNLOADING ---

update = input(f"Found version {newer}, wish to update? [y/n]: ")
while update not in ("y", "n"):
    update = input(f"Found version {newer}, wish to update? [y/n]: ")

if update == "n":
    print("Update cancelled.")
    exit(0)

print("Downloading new version...")

if not os.path.exists(down_folder):
    print(f"{down_folder} not found, creating one.")
    os.mkdir(down_folder)

for file in utilities.files:
    r = requests.get(f"{base_url}{file}")
    if not r.ok:
        print(f"Request to {base_url}{file} had response {r}")
        print(f"Exception: {r}")
        exit(1)
    with open(f"{down_folder}/{file}", "w") as f:
        f.write(r.text)


# --- MOVING FILES TO DESTINATION ---

print(f"Moving files to base folder {utilities.dest_path}")
for file in utilities.files:
    subprocess.run(["mv", f"{down_folder}/{file}", f"{utilities.dest_path}/{file}"])

subprocess.run(["mv", f"{utilities.dest_path}/notify.py", f"{utilities.dest_path}/python_module/notify.py"])

if os.path.exists(f"{utilities.dest_path}/{update_setup_file}"):
    subprocess.run(["python3", f"{utilities.dest_path}/{update_setup_file}"])

print("Update completed.")