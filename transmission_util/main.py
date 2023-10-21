from datetime import datetime,timezone,timedelta

from transmission_rpc import Client

ssd_path = "/Users/martina/media/"
ssd_path = "/Volumes/MyBookAPFS/Media/"
hdd_path = "/Volumes/Seagate2/"
hdd_path = "/Volumes/MyBookAPFS/Media2/"

def main():
    c = Client(host="192.168.1.12", port=9091)
    now = datetime.now().astimezone(timezone.utc)
    delta = timedelta(days=30)
    cutoff = now - delta
    torrents = c.get_torrents(None, ["doneDate","id","downloadDir"])
    ssd_torrents = [t for t in torrents if t.download_dir.startswith(ssd_path)]
    old_ssd_torrents =  [t for t in ssd_torrents if t.done_date and t.done_date > cutoff]
    for torrent in old_ssd_torrents:
        new_path = torrent.download_dir.replace(ssd_path, hdd_path)
        print(torrent.download_dir, new_path)
        c.move_torrent_data(torrent.id, new_path)


if __name__ == "__main__":
    main()
