from datetime import datetime,timezone,timedelta

from transmission_rpc import Client
import argparse
import sys


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

    sys.exit(1)



if __name__ == "__main__":
    main()
