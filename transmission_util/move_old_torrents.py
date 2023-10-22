from datetime import datetime,timezone,timedelta

from transmission_rpc import Client

ssd_path = "/Users/martina/media/"
hdd_path = "/Volumes/Seagate2/"

def main():
    c = Client(host="192.168.1.12", port=9091)
    now = datetime.now().astimezone(timezone.utc)
    delta = timedelta(days=30)
    cutoff = now - delta
    torrents = c.get_torrents(None, ["doneDate","id","name","downloadDir"])
    print(f"A total of {len(torrents)} torrents being tracked")
    ssd_torrents = [t for t in torrents if t.download_dir.startswith(ssd_path)]
    print(f"{len(ssd_torrents)} torrents on the SSD")
    old_ssd_torrents = [t for t in ssd_torrents if t.done_date and t.done_date > cutoff]
    print(f"{len(old_ssd_torrents)} old torrents on the SSD")
    for torrent in old_ssd_torrents:
        new_path = torrent.download_dir.replace(ssd_path, hdd_path)
        print(f"Moving torrent #{torrent.id} '{torrent.name}' from '{torrent.download_dir}' to '{new_path}'")
        c.move_torrent_data(torrent.id, new_path)


if __name__ == "__main__":
    main()
