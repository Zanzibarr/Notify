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
    utilities.ntf_print(f"Request to {base_url}{version_control} had response {r}", on_file=log_to_file)
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
    utilities.ntf_print("notify is already up-to-date.", on_file=log_to_file)
    exit(0)


# --- DOWNLOADING ---

update = input(f"Found version {newer}, wish to update? [y/n]: ")
while update not in ("y", "n"):
    update = input(f"Found version {newer}, wish to update? [y/n]: ")

if update == "n":
    print("Update cancelled.")
    exit(0)

if not os.path.exists(down_folder):
    utilities.ntf_print(f"{down_folder} not found, creating one.", on_file=log_to_file)
    os.mkdir(down_folder)

for file in utilities.files:
    r = requests.get(f"{base_url}{file}")
    if not r.ok:
        utilities.ntf_print(f"Request to {base_url}{file} had response {r}", on_file=log_to_file)
        print(f"Exception: {r}")
        exit(1)
    with open(f"{down_folder}/{file}", "w") as f:
        f.write(r.text)


# --- MOVING FILES TO DESTINATION ---

utilities.ntf_print(f"Moving files to base path {utilities.dest_path}", on_file=log_to_file)
for file in utilities.files:
    subprocess.run(["cp", f"{down_folder}/{file}", f"{utilities.dest_path}/{file}"])

subprocess.run(["mv", f"{down_folder}/notify.py", f"{utilities.dest_path}/python_module/notify.py"])

#subprocess.run(["rm", "-r", down_folder])

if os.path.exists(f"{utilities.dest_path}/{update_setup_file}"):
    subprocess.run(["python3", f"{utilities.dest_path}/{update_setup_file}"])

utilities.ntf_print("Update completed.", on_file=log_to_file)