from datetime import datetime,timezone,timedelta

from transmission_rpc import Client
import argparse
import sys
import re


def main():
    parser = argparse.ArgumentParser(description='A program to check for torrent duplicates')
    # parser.add_argument('arg1', type=int, help='An integer argument')
    parser.add_argument('--episode', type=int, help='The episode number', required=True)
    parser.add_argument('--season', type=int, help='The season number', required=True)
    parser.add_argument('--title', type=str, help='The show title', required=True)

    args = parser.parse_args()
    
    print(f'title: {args.title}')
    print(f'season: {args.season}')
    print(f'episode: {args.episode}')

    title_without_spaces = args.title.replace(" ", ".")
    episode_season = f"S{args.season:02}E{args.episode:02}"
    pattern_str = f"^{title_without_spaces}.+{episode_season}.+"
    
    print(f"Using this regexp to check torrents names: '{pattern_str}'")
    pattern = re.compile(pattern_str, re.IGNORECASE)

    c = Client(host="192.168.1.12", port=9091)
    torrents = c.get_torrents(None, ["name"])
    matched_torrents = [t for t in torrents if re.match(pattern, t.name)]

    for torrent in matched_torrents:
        print(f"Matched torrent: {torrent}")
    
    if matched_torrents:
        sys.exit(1)
    
    sys.exit(2)



if __name__ == "__main__":
    main()
