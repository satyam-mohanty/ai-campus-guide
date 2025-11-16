import tkinter as tk
from tkinter import scrolledtext, ttk, END
import sys
try:
    from utils import get_greeting, opening_prompt, normalize_text
    from bot_cli import find_entity, detect_intent, format_response
except ImportError as e:
    print(f"Error: Missing required file. Make sure kb.py, utils.py, and bot_cli_2.py are in the same directory.")
    print(f"Details: {e}")
    sys.exit()
BG_COLOR = "#fbfaf8"             
CHAT_BG = "#ffffff"             
INPUT_BG = "#ffffff"            
USER_COLOR = "#2a2a2a"             
GUIDE_COLOR = "#4a4a4a"            
SYSTEM_COLOR = "#9a9a9a"            
BUTTON_BG = "#2a2a2a"             
BUTTON_FG = "#ffffff"              
BUTTON_ACTIVE_BG = "#1a1a1a"        
BORDER_COLOR = "#f0f0f0"           

FONT_HEADER = ("Inter", 18, "bold")    
FONT_NORMAL = ("Inter", 12)        
FONT_BOLD = ("Inter", 12, "bold")    
FONT_SMALL_ITALIC = ("Inter", 11, "italic") 

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Campus Guide")
        self.root.geometry("500x650") 
        self.root.configure(bg=BG_COLOR) 
        
        
        self.last_entity = None

        

        
        self.main_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        
        header_label = tk.Label(
            self.main_frame, 
            text="Virtual Campus Guide", 
            font=FONT_HEADER, 
            bg=BG_COLOR, 
            fg=USER_COLOR 
        )
        header_label.grid(row=0, column=0, sticky="w", pady=(0, 20))

        chat_frame = tk.Frame(
            self.main_frame, 
            bg=BORDER_COLOR, 
            bd=1,
            relief="solid"
        )
        chat_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 20))
        
        self.chat_area = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            state="disabled",
            font=FONT_NORMAL,
            bg=CHAT_BG,
            fg=GUIDE_COLOR,
            padx=15,
            pady=15,
            bd=0,
            highlightthickness=0, 
            relief="flat"
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True)
        
        
        self.chat_area.tag_configure("user", foreground=USER_COLOR, font=FONT_BOLD)
        self.chat_area.tag_configure("guide", foreground=GUIDE_COLOR, font=FONT_NORMAL)
        self.chat_area.tag_configure("system", foreground=SYSTEM_COLOR, font=FONT_SMALL_ITALIC)

        
        self.input_frame = tk.Frame(
            self.main_frame, 
            bg=INPUT_BG,
            highlightbackground=BORDER_COLOR, 
            highlightthickness=1 
        )
        self.input_frame.grid(row=2, column=0, sticky="ew")

        
        self.user_entry = tk.Entry(
            self.input_frame,
            font=FONT_NORMAL,
            bg=INPUT_BG,
            fg=USER_COLOR, 
            relief="flat", 
            bd=0,
            width=40 
        )
        self.user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=15, pady=15)
        
       
        self.user_entry.bind("<Return>", self.send_message)

        
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            font=FONT_BOLD,
            command=self.send_message,
            bg=BUTTON_BG,
            fg=BUTTON_FG,
            activebackground=BUTTON_ACTIVE_BG,
            activeforeground=BUTTON_FG,
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2" 
        )
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)
       
        self.display_message(get_greeting(), "system")
        self.display_message(opening_prompt(), "guide")

    def display_message(self, message, tag="guide"):
        """Inserts a message into the chat area with the correct tag and scrolls down."""
        self.chat_area.config(state="normal") 
        
        if tag == "user":
            self.chat_area.insert(tk.END, f"You: {message}\n\n", ("user",)) 
        else:
            self.chat_area.insert(tk.END, f"Guide: {message}\n\n", (tag,))
        
        self.chat_area.config(state="disabled") 
        self.chat_area.see(tk.END) 

    def send_message(self, event=None):
        """Handles sending the user's message and getting a response."""
        user_input = self.user_entry.get().strip()
        
        if not user_input:
            return 
        
        
        self.display_message(user_input, "user")
        
        
        self.user_entry.delete(0, tk.END)

        
        if user_input.lower() in ("exit", "quit"):
            self.display_message("Goodbye! Have a great day.", "guide")
            
            self.root.after(1000, self.root.destroy)
            return

        
        self.get_bot_response(user_input)

    def get_bot_response(self, user_input):
        """Processes the user input and generates the bot's response."""
        text = normalize_text(user_input)
        entity = find_entity(text)
        
        response = ""
        if entity:
            self.last_entity = entity
            intent = detect_intent(text)
            response = format_response(entity, intent)
        elif self.last_entity and "it" in text:
            
            response = format_response(self.last_entity, "summary")
        else:
            response = "Sorry, I don’t have information about that yet."
            
        
        self.display_message(response, "guide")

if __name__ == "__main__":
    try:
        import fuzzywuzzy
    except ImportError:
        print("Error: 'fuzzywuzzy' library not found.")
        print("Please install it by running: pip install fuzzywuzzy python-Levenshtein")
        sys.exit()

    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()