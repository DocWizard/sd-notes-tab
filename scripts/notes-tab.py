import modules.scripts as scripts
import gradio as gr
import os

from modules import script_callbacks

current_extension_directory = scripts.basedir()
PERSISTENCE_FILE = os.path.join(scripts.basedir(), "textbox_content.txt")


# Function to save the textbox content to a file
def save_content(content):
    with open(PERSISTENCE_FILE, "w") as f:
        f.write(content)

# Function to load the textbox content from a file
def load_content():
    if os.path.exists(PERSISTENCE_FILE):
        with open(PERSISTENCE_FILE, "r") as f:
            return f.read()
    return ""

def on_ui_tabs():
    # Load the initial content from the file
    initial_content = load_content()

    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            textbox = gr.Textbox(
                value=initial_content,
                label="My notes:",
                lines=10  # Set the number of lines for multiline input
            )

            # Define the function to handle textbox blur event
            def handle_blur(textbox_content):
                save_content(textbox_content)
                return "Content saved!"

            # Link the blur event to the handle_blur function
            textbox.blur(handle_blur, inputs=textbox, outputs=[])

        return [(ui_component, "Notes", "notes_tab")]

# Call on_ui_tabs() at the beginning to ensure initial content loading
on_ui_tabs()
script_callbacks.on_ui_tabs(on_ui_tabs)
