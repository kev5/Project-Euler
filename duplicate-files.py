'''
We walk through our whole file system iteratively. As we go, we take a "fingerprint" of each file in constant time
by hashing the first few, middle few, and last few bytes. We store each file's fingerprint in a dictionary as we go.

If a given file's fingerprint is already in our dictionary, we assume we have a duplicate. In that case, we assume
the file edited most recently is the duplicate one.

We've made a few assumptions here:

1. Two different files won't have the same fingerprints: It's not impossible that two files with different contents will
have the same beginning, middle, and end bytes so they'll have the same fingerprints. Or they may even have different
sample bytes but still hash to the same value (this is called a "hash collision"). To mitigate this, we could do a
last-minute check whenever we find two "matching" files where we actually scan the full file contents to see if they're the same.

2. The most recently edited file is the duplicate: This seems reasonable, but it might be wrong—for example, there might be
files which have been edited by daemons (programs that run in the background) after our friend finished duplicating them.

3. Two files with the same contents are the same file. This seems trivially true, but it could cause some problems.
For example, we might have empty files in multiple places in our file system that aren't duplicates of each-other.

Complexity:

Each "fingerprint" takes O(1)O(1) time and space, so our total time and space costs are O(n) where n is the number of files
on the file system.

If we add the last-minute check to see if two files with the same fingerprints are actually the same files (which we probably should),
then in the worst case all the files are the same and we have to read their full contents to confirm this, giving us a runtime
that's order of the total size of our files on disc.
'''

import os
import hashlib

def find_duplicate_files(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]

    # We'll track tuples of (duplicate_file, original_file)
    duplicates = []

    while len(stack):
        current_path = stack.pop()

        # If it's a directory,
        # put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # If it's a file
        else:
            # Get its hash
            file_hash = sample_hash_file(current_path)

            # Get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # If we've seen it before
            if file_hash in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_hash]
                if current_last_edited_time > existing_last_edited_time:
                    # Current file is the dupe!
                    duplicates.append((current_path, existing_path))
                else:
                    # Old file is the dupe!
                    duplicates.append((existing_path, current_path))
                    # But also update files_seen_already to have
                    # the new file's info
                    files_seen_already[file_hash] = (current_last_edited_time, current_path)

            # If it's a new file, throw it in files_seen_already
            # and record its path and last edited time,
            # so we can tell later if it's a dupe
            else:
                files_seen_already[file_hash] = (current_last_edited_time, current_path)

    return duplicates


def sample_hash_file(path):
    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)
    hasher = hashlib.sha512()

    with open(path, 'rb') as file:
        # If the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())
        else:
            num_bytes_between_samples = (
                (total_bytes - num_bytes_to_read_per_sample * 3) / 2
            )

            # Read first, middle, and last bytes
            for offset_multiplier in xrange(3):
                start_of_sample = (
                    offset_multiplier
                    * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                )
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()
