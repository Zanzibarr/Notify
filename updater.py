import requests, utilities, subprocess, sys, os

base_url = "https://raw.githubusercontent.com/Zanzibarr/Telegram_Python_Notifier/main/"
version_control = "change_log.md"
update_setup_file = "update_setup.py"

down_folder = f"{utilities.base_path}/Downloads"


# --- LOGGING OPTIONS ---

if len(sys.argv) == 2 and sys.argv[1] not in ("d", "s", "ds"):
    print("Wrong arguments.")
    exit(1)
log_to_file = "s" in sys.argv[1]


# --- VERSION CONTROL ---

r = requests.get(f"{base_url}{version_control}")

if not r.ok:
    utilities.ntf_print(f"Request to {base_url}{version_control} had response {r}", on_file=log_to_file)
    print(f"Exception: {r}")
    exit(1)

text = r.text

update = True
dev = "d" in sys.argv[1]
newer = text.partition("Version ")[2].partition("\n")[0]

if not dev:
    a, _, rest = utilities.version.partition(": ")[2].partition(".")
    old = f"{a}.{rest.partition('.')[0]}"
    a, _, rest = newer.partition(": ")[2].partition(".")
    new = f"{a}.{rest.partition('.')[0]}"
    update = new == old

if not update:
    utilities.ntf_print("notify is already up-to-date.", on_file=log_to_file)
    exit(0)


# --- DOWNLOADING ---

if not os.path.exists(down_folder):
    utilities.ntf_print(f"{down_folder} not found, creating one.", on_file=log_to_file)
    os.mkdir(down_folder)

for file in utilities.files:
    r = requests.get(f"{base_url}{file}")
    if not r.ok:
        utilities.ntf_print(f"Request to {base_url}{file} had response {r}", on_file=log_to_file)
        print(f"Exception: {r}")
        exit(1)
    if not os.path.exists(f"{down_folder}/{file}"):
        open(f"{down_folder}/{file}", "x")
    with open(f"{down_folder}/{file}", "w") as f:
        f.write(r.text)


# --- MOVING FILES TO DESTINATION ---

utilities.ntf_print(f"Moving files to base path {utilities.dest_path}")
for file in utilities.files:
    subprocess.run(["cp", f"{down_folder}/{file}", f"{utilities.dest_path}/{file}"])

subprocess.run(["mv", f"{down_folder}/notify.py", f"{utilities.dest_path}/python_module/notify.py"])

subprocess.run(["rm", "-r", down_folder])

if os.path.exists(f"{utilities.dest_path}/{update_setup_file}"):
    subprocess.run(["python3", f"{utilities.dest_path}/{update_setup_file}"])

utilities.ntf_print("Update completed.", on_file=log_to_file)