import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os



class LogFileParserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Log File Parser")
        self.root.geometry("1000x800")

        self.current_file = None

        ##Container to stack the frames
        container = tk.Frame(root)
        container.pack(fill="both", expand=True)

        #dictionary to hold frames.
        self.frames = {}

        #create both screens
        for F in (MainScreen, OutputScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainScreen)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

        if frame_class == OutputScreen:
            frame.load_and_display_file()

    def select_file(self):
        filepath = filedialog.askopenfilename(title="Select a file", filetypes=[("Log Files", "*.log"), ("All files", "*.*")])
        if filepath:
            self.current_file = filepath
            self.show_frame(OutputScreen)

    def get_parsed_content(self, filepath):
        ##logic for parsing content
        errors = []
        warnings = []
        timing_summary = []
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    if 'error' in line.lower():
                        errors.append(line.strip())
                    elif 'warning' in line.lower():
                        warnings.append(line.strip())
                    elif 'Timing Summary' in line:
                        timing_summary.append(line.strip())
        except Exception as e:
            return f"Failed to read / Parse file: \n {str(e)}"
        
        output_lines = []

        if errors:
            output_lines.append("=== ERRORS ===")
            output_lines.extend(errors)
            output_lines.append("")
        
        if warnings:
            output_lines.append("=== WARNINGS ===")
            output_lines.extend(warnings)
            output_lines.append("")

        if timing_summary:
            output_lines.append("=== TIMING SUMMARY ===")
            output_lines.extend(timing_summary)
            output_lines.append("")

        if not output_lines:
            output_lines.append("No errors, warnings or timing summaries found in file.")

        return "\n".join(output_lines)

class MainScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Choose a file to parse:")
        label.pack(pady=50)

        btn = tk.Button(self, text="Browse...", command=self.controller.select_file, width=20, height=2)
        btn.pack()


class OutputScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Button frame (Back + Refresh)
        button_frame = tk.Frame(self)
        button_frame.pack(anchor="nw", padx=10, pady=5)

        back_btn = tk.Button(button_frame, text="← Back", command=lambda: controller.show_frame(MainScreen))
        back_btn.pack(side="left", padx=(0, 10))

        refresh_btn = tk.Button(button_frame, text="Refresh", command=self.load_and_display_file)
        refresh_btn.pack(side="left")

        # Text widget with scrollbar
        text_frame = tk.Frame(self)
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.text_box = tk.Text(text_frame, wrap="word")
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=scrollbar.set)

        self.text_box.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def load_and_display_file(self):
        """Read, parse, and display the current file."""
        if not self.controller.current_file or not os.path.exists(self.controller.current_file):
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, "No valid file selected or file was deleted.")
            return

        content = self.controller.get_parsed_content(self.controller.current_file)
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, content)


#run app
if __name__ == "__main__":
    root = Tk()
    app = LogFileParserApp(root)
    root.mainloop()
