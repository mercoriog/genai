from zipfile import ZipFile
import gdown
import time
import os

def deleteFile(file):
    # Notify deleting operation.
    print(f"[DEL] Deleting file: {file}")

    # Set an exceptions handler:
    try:
        # Delete file from path.
        os.remove(file)

        # Notify deleting done.
        print(f"[DEL] File deleted with no errors.")

    # An error occurs:
    except Exception as e:
        # Notify error.
        print(f"[ERROR] Deleting ZIP file failed. Message: ", e)

def extractPathTo(filename):
    # This function split file's path in two parts.
    path_to, basename = os.path.split(filename)

    # Return path to file part.
    return path_to

def getUnzipFolder(file_path):
    # Extract the 'path to' part from file path
    unzip_to = extractPathTo(file_path)

    # Return folder where to unzip the file.
    return unzip_to

def unzipFile(file, unzip_folder):
    # Notify unzip operation.
    print(f"[UNZIP] Unzip file: {file}")
    
    # Set an exceptions handler:
    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(file) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(unzip_folder)

        # Notify correct result.
        print("[UNZIP] File unzipped with no errors.")
    
    # An error occurs:
    except Exception as e:
        # Notify error.
        print(f"[ERROR] Unzip failed. Message: ", e)

        # Return False if any error occurs.
        return False

    # This function returns True if no error occurs.
    return True

def downloadFile(url, save_path):
    # Notify downloadinf file.
    print(f"[DOWN] Downloading URL: {url}")

    # Set an exceptions handler:
    try:
        # Download file with <url> and store it at <save_path>.
        # Set 'fuzzy=True' param if url is copy-pasted from Google Drive direct link.
        gdown.download(url, save_path, fuzzy=True)
        
        # Notify downloaded file.
        print(f"[DOWN] File downloaded with no errors.\n[DOWN] Downloaded file stored at: {save_path}")

    # An error occurs:
    except Exception as e:
        # Notify error.
        print(f"[ERROR] Download failed. Message: ", e)
        
        # Return False if any error occurs.
        return False

    # This function returns True if no error occurs.
    return True

def downloadAndUnzip(url, save_path, delete_when_unzipped):
    # Download file at <url> and store at <save_path>.
    downloaded = downloadFile(url, save_path)

    # Check if file is downloaded with no errors:
    if not downloaded:
        # Return False if any error occurs.
        return False
    
    # Get folder path where to unzip file.
    unzip_folder = getUnzipFolder(save_path)

    # Unzip downloaded file.
    unzipped = unzipFile(save_path, unzip_folder)

    # Check if file is unzipped with no errors:
    if not unzipped:
        # Return False if any error occurs.
        return False

    # Check if ZIP file has to be deleted:
    if delete_when_unzipped == True:
        # Delete ZIP File.
        deleted = deleteFile(save_path)

    # This function returns True if no error occurs.
    return True