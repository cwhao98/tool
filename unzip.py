import sys, os, zipfile

def unzip_single(src_file, dest_dir, password=None):
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir, pwd=password)
    except RuntimeError as e:
        print(e)
    zf.close()

def unzip_all(source_dir, dest_dir, password):
    if not os.path.isdir(source_dir): 
        unzip_single(source_dir, dest_dir, password)
    else:
        it = os.scandir(source_dir)
        for entry in it:
            if entry.is_file() and os.path.splitext(entry.name)[1]=='.zip' :
                unzip_single(entry.path, dest_dir, password)

def get_release_scans(release_file):
    scan_lines = open(release_file)
    scans = []
    for scan_line in scan_lines:
        scan_id = scan_line.rstrip('\n')
        scans.append(scan_id)
    return scans

if __name__ == "__main__":

    release_file = 'data/v1/scans.txt'
    scans = get_release_scans(release_file)
    for scan in scans:
        src = os.path.join('data/v1/scans/',scan,'matterport_skybox_images.zip')
        dest_dir = 'data/v1/scans/'
        unzip_single(src, dest_dir)
