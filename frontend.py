import PySimpleGUI as SimpGUI
from functions import extract_archive

file_input = SimpGUI.Input()
file_button = SimpGUI.FileBrowse("File")

destination_input = SimpGUI.Input()
destination_button = SimpGUI.FolderBrowse("Destination")

extract_button = SimpGUI.Button("Extract")
output_label = SimpGUI.Text(text_color="green", key="output")

window = SimpGUI.Window(layout=[[file_input, file_button],
                                [destination_input, destination_button],
                                [extract_button, output_label]],
                        title="File Extractor")

while True:
    # values gets a dict with filepaths - File:"/../.." Destination:"/../.."
    event, values = window.read()
    print(event, values)
    print(values["File"], values["Destination"])

    if event == SimpGUI.WIN_CLOSED:
        break

    elif event == "Extract":
        print("Extract")
        extract_archive(values["File"], values["Destination"])
        window["output"].update("Extracted!")

