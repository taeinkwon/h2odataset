import tqdm
import argparse
import requests
import os
from pathlib import Path

def downloader(url, dest, user, password, resume_byte_pos=None):
    local_filename = url.split('/')[-1]
    # Header information
    r = requests.head(url, stream=True, auth=(user, password))
    resume_header = ({'Range': f'bytes={resume_byte_pos}-'}
                     if resume_byte_pos else None)
    total_size_in_bytes = int(r.headers.get('content-length', 0))

    # File
    r = requests.get(url, stream=True, auth=(user, password),headers=resume_header)
    block_size = 8192
    initial_pos = resume_byte_pos if resume_byte_pos else 0
    mode = 'ab' if resume_byte_pos else 'wb'

    progress_bar = tqdm.tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, unit_divisor=block_size,
                  desc=local_filename, initial=initial_pos, ascii=True, miniters=1)
    with open(os.path.join(dest, local_filename), mode) as f:
        for chunk in r.iter_content(chunk_size=block_size): 
            progress_bar.update(len(chunk))
            f.write(chunk)
    progress_bar.close()


def download_file(url, dest, user, password):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True, auth=(user, password))
    r.raise_for_status()   
    total_size_in_bytes = int(r.headers.get('content-length', 0))
    file_path = os.path.join(dest,local_filename)
    if os.path.exists(file_path):
        file_size_offline = Path(file_path).stat().st_size
        if total_size_in_bytes != file_size_offline:
            print(f'File {local_filename} is incomplete. Resume download.')
            downloader(url, dest, user, password, file_size_offline)
        else:
            print(f'File {local_filename} is complete. Skip download.')
    else:
        downloader(url, dest, user, password)
    return local_filename

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download H2O")
    parser.add_argument('--mode', type=str, default='ego', choices=['all', 'ego', 'pose'],
                        help = 'Download all views, an egocentric view, or only poses')
    parser.add_argument('--dest', type=str,help = 'Destination path to download files.', default='downloads')
    parser.add_argument('--username', type=str,help = 'id from https://h2odataset.ethz.ch/', required=True)
    parser.add_argument('--password', type=str,help = 'password from https://h2odataset.ethz.ch/',required=True)

    args = parser.parse_args()
    url = 'https://h2odataset.ethz.ch/data/dataset/'
    if args.mode == 'all':
        file_name_list = +['object.zip','label_split.zip','subject1_v1_1.tar.gz','subject2_v1_1.tar.gz','subject3_v1_1.tar.gz','subject4_v1_1.tar.gz']
    elif args.mode == 'ego':
        file_name_list = ['object.zip','label_split.zip','subject1_ego_v1_1.tar.gz','subject2_ego_v1_1.tar.gz','subject3_ego_v1_1.tar.gz','subject4_ego_v1_1.tar.gz']
    elif args.mode == 'pose':
        file_name_list = ['object.zip','label_split.zip','subject1_pose_v1_1.tar.gz','subject2_pose_v1_1.tar.gz','subject3_pose_v1_1.tar.gz','subject4_pose_v1_1.tar.gz']
    file_list =  [url + s for s in file_name_list]

    if not os.path.exists(args.dest):
        os.makedirs(args.dest)

    for file_url in tqdm.tqdm(file_list):
        download_file(file_url, args.dest, args.username, args.password)