import requests, utilities, subprocess, sys, os

base_url = "https://raw.githubusercontent.com/Zanzibarr/Notify/main/"
version_control = "change_log.md"
update_setup_file = "update_setup.py"

down_folder = f"{utilities.base_path}/Downloads"


# --- LOGGING OPTIONS ---

if len(sys.argv) == 2 and sys.argv[1] not in ("d", "s", "ds"):
    utilities.print_exception("Wrong arguments.")
    
log_to_file = len(sys.argv) == 2 and "s" in sys.argv[1]


# --- VERSION CONTROL ---

try:
    r = requests.get(f"{base_url}{version_control}")
except Exception as e:
    utilities.print_exception(f"Requests module exception: {e}")

if not r.ok:
    utilities.print_exception(f"Request to {base_url}{version_control} had response {r}")

text = r.text

update = True
dev = len(sys.argv) == 2 and "d" in sys.argv[1]
newer = text.partition("Version ")[2].partition("\n")[0]
log = text.partition("\n")[2].partition("#")[0]

if not dev:
    o_v, o_p = utilities.version.partition(": ")[2].split(".")[:2]
    n_v, n_p = newer.split(".")[:2]
    update = o_v+o_p != n_v+n_p

if not update:
    utilities.print_info("notify is already up-to-date.")
    exit(0)


# --- DOWNLOADING ---

utilities.print_info(f"Found version {newer}\n\nVersion changelog:\n{log}")
update = utilities.print_input(f"{utilities.cmd_input}Wish to update?{utilities.cmd_end} [y/n]: ")
while update not in ("y", "n"):
    utilities.print_warning("Command not recognised.")
    update = utilities.print_input(f"Found version {newer}, {utilities.cmd_input}wish to update?{utilities.cmd_end} [y/n]: ")

if update == "n":
    utilities.print_warning("Update cancelled.")
    exit(0)

utilities.print_info("Downloading new version...")

if not os.path.exists(down_folder):
    utilities.print_info(f"{down_folder} not found, creating one.")
    os.mkdir(down_folder)

for file in utilities.files:
    try:
        r = requests.get(f"{base_url}{file}")
    except Exception as e:
        utilities.print_exception(f"Requests module exception: {e}")
    if not r.ok:
        utilities.print_exception(f"Request to {base_url}{file} had response {r}")
        
    with open(f"{down_folder}/{file}", "w") as f:
        f.write(r.text)


# --- MOVING FILES TO DESTINATION ---

utilities.print_info(f"Moving files to base folder {utilities.dest_path}")
for file in utilities.files:
    subprocess.run(["mv", f"{down_folder}/{file}", f"{utilities.dest_path}/{file}"])

subprocess.run(["mv", f"{utilities.dest_path}/notify.py", f"{utilities.dest_path}/python_module/notify.py"])

utilities.print_info("Running update setup.")
if os.path.exists(f"{utilities.dest_path}/{update_setup_file}"):
    subprocess.run(["python3", f"{utilities.dest_path}/{update_setup_file}"])

utilities.print_info("Update completed.")