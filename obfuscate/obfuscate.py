import os
import random
import string
import hashlib
from PIL import Image
import shutil


bits = 8


def obfuscate(path, obfuscate_filenames = True, save_order = True, compress_quality = 100, write_changes = False):
    for path, folders, files in os.walk(path):
        files.sort(key=lambda f: int(''.join(filter(str.isdigit, f)) or -1))
        index = 0
        total = len(files)
        if total > 10 ** bits:
            print('PASSED: low bits for a lot of files')
            continue
        else:
            print(f'{path} files total: {total}')
        for file in files:
            if obfuscate_filenames:
                name, ext = os.path.splitext(os.path.join(path, file))
                if not save_order:
                    mask = string.digits + string.ascii_uppercase
                    target = ''.join(random.choice(mask) for i in range(bits)) + str(ext).lower()
                else:
                    mask = string.ascii_uppercase
                    prefix_width = len(str(total))
                    target = f'{index:0{prefix_width}d}' + ''.join(random.choice(mask) for i in range(bits-prefix_width)) + str(ext).lower()
            else:
                target = file
            print(f'{file[:24]:<24} -> {target}')
            if write_changes:
                os.rename(os.path.join(path, file), os.path.join(path, target))
                if compress_quality != 100 and (file.endswith('.jpg') or file.endswith('.jpeg')):
                    compress_jpeg(os.path.join(path, target), compress_quality)
            index += 1
    return 0


def check_dublicates(path):
    dublicate_counter = 0
    files = []
    for path, folders, files in os.walk(path):
        files.sort(key=lambda f: int(''.join(filter(str.isdigit, f)) or -1))
    digests = dict()
    for file in files:
        with open(os.path.join(path, file), 'rb') as f:
            digest = hashlib.md5(f.read()).hexdigest()
            if digest in digests.values():
                print(f'{file} == {[k for k, v in digests.items() if v == digest][0]}')
                dublicate_counter += 1
            digests[file] = digest
    return dublicate_counter


def compress_jpeg(path, compress_quality = 85):
    try:
        with Image.open(path) as img:
            img.save(path, "JPEG", quality=compress_quality)
    except Exception as e:
        print(f'Compress image error {path}: {e}')


if __name__ == "__main__":
    while (True):
        path = input('\nInput Path and press Enter to continue...\n')
        while dublicates := check_dublicates(path) != 0:
            if not bool(input('Duplicate files with different names were found in the specified path. Fix it and press Enter (RECOMMENDED) to repeat or type any value to continue anyway?\n')):
                continue
            else:
                break
        obfuscate_filenames = not bool(input('Enable obfuscation? Press Enter to enable random renaming files (RECOMMENDED) or type any value to disable (save original file names)\n'))
        if obfuscate_filenames:
            save_order = not bool(input('Keep the original alphabetical order? Press Enter to keep (RECOMMENDED) or type any value to not keep (random)\n'))
        else:
            save_order = True
        compress_images = bool(input('Compress photos? Press Enter now to pass (RECOMMENDED) or type any value to compress photos\n'))
        if compress_images:
            try:
                compress_quality = int(input('Setup compression quality level 1 .. 99 (85 RECOMMENDED) and press Enter\n'))
                if not (1 <= compress_quality <= 99):
                    print('Compression quality level out of range! Setting default value: 85')
                    compress_quality = 85
            except ValueError:
                print('Compression quality level out of range! Setting default value: 85')
                compress_quality = 85
        else:
            compress_quality = 100
        print(f'{path=}, {obfuscate_filenames=}, {save_order=}, {compress_images=}, {compress_quality=}')
        write_changes = bool(input('Write changes? Press Enter now to preview only (RECOMMENDED) or type any value to write changes immediately\n'))
        obfuscate(path, obfuscate_filenames, save_order, compress_quality, write_changes)