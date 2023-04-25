import zipfile

with zipfile.ZipFile("example.zip", "r") as zip_ref:
    zip_ref.extractall("extracted_folder")
##################################################
import tarfile

with tarfile.open("example.tar.gz", "r:gz") as tar_ref:
    tar_ref.extractall("extracted_folder")

##################################################
import gzip

with gzip.open("example.gz", "rb") as gz_ref:
    with open("example", "wb") as file_ref:
        file_ref.write(gz_ref.read())
##################################################
import bz2

with bz2.BZ2File("example.bz2", "rb") as bz2_ref:
    with open("example", "wb") as file_ref:
        file_ref.write(bz2_ref.read())
##################################################

import tarfile

with tarfile.open("example.tar.gz", "r:gz") as tar_ref:
    tar_ref.extractall("extracted_folder")

import patoolib

patoolib.extract_archive("example.rar", outdir="extracted_folder")


import py7zr

with py7zr.SevenZipFile('example.7z', mode='r') as archive:
    archive.extractall(path='extracted_folder')
