import zipfile


def extract_archive(file_path, destination_path):
    with zipfile.ZipFile(file_path, "r") as archive:
        archive.extractall(destination_path)


# Test
if __name__ == "__main__":
    extract_archive("C:/Users/charl/OneDrive/Pictures/ziptest/compressed.zip",
                    "C:/Users/charl/Programming/mega/CodingExercises/file_extractor/files")
