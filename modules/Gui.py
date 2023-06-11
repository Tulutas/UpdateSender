import tkinter as tk
from tkinter import filedialog

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("600x400")  # Set window size to 600x400
        self.pack(fill=tk.BOTH, expand=True)  # Fill window with frame
        self.create_widgets()

    def create_widgets(self):
        # Create label and entry for the file selector
        self.file_label = tk.Label(self, text="Select a file:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.file_entry = tk.Entry(self, state='readonly', width=50)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10)
        self.file_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.file_button.grid(row=0, column=2, padx=10, pady=10)

        # Create labels and entries for the text inputs
        self.label1 = tk.Label(self, text="Enter IP Address:")
        self.GivenIP = tk.Entry(self, validate='key')
        self.GivenIP.config(validatecommand=(self.register(self.validate_ip_address), '%P'))
        self.label2 = tk.Label(self, text="Enter Port Number:")
        self.GivenPort = tk.Entry(self, validate='key')
        self.GivenPort.config(validatecommand=(self.register(self.validate_port_number), '%P'))

        # Pack the labels and entries
        self.label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.GivenIP.grid(row=1, column=1, padx=10, pady=10)
        self.label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.GivenPort.grid(row=2, column=1, padx=10, pady=10)

        # Create button to submit values
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_values)
        self.submit_button.grid(row=3, column=1, padx=10, pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Hex files", "*.hex")])
        if file_path:
            if not file_path.endswith(('.hex', '.txt')):
                tk.messagebox.showerror("Error", "Invalid file type. Please select a .hex or .txt file.")
                return
            self.file_entry.config(state='normal')
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
            self.file_entry.config(state='readonly')

    def validate_ip_address(self, ip_address):
        """
        Validates whether the input is a valid IP address.
        """
        try:
            import ipaddress
            if '.' in ip_address:
                segments = ip_address.split('.')
                for segment in segments:
                    if not segment.isdigit() or int(segment) < 0 or int(segment) > 255:
                        return False
                # All segments are valid integers between 0 and 255, so we can create an IPv4Address object
                ipaddress.IPv4Address(ip_address)
            else:
                # If there are no periods in the input string, it may be an IPv6 or domain name representation of an IP address
                ipaddress.ip_address(ip_address)
            return True
        except ValueError:
            if len(ip_address) < 4:
                # If the input is a single digit, it's a valid input even though it's not a complete IP address
                return True
            elif (len(ip_address)==3) and not ip_address.isdigit() or int(ip_address) < 0 or int(ip_address) > 255 :
                return True
            elif (len(ip_address)==4) and not ip_address[0:2].isdigit() or int(ip_address[0:2]) < 0 or int(ip_address[0:2]) > 255 and ip_address(3)==".":
                return      
            else:
                return False

    def validate_port_number(self, port_number):
        """
        Validates whether the input is a valid port number.
        """
        try:
            port = int(port_number)
            if 0 <= port <= 65535:
                return True
            else:
                return False
        except ValueError:
            return False

    def submit_values(self):
        # Get values from entries
        file_path = self.file_entry.get()
        GivenIP = self.GivenIP.get()
        GivenPort = self.GivenPort.get()

        # Check if input fields are empty or invalid
        if not all([file_path, self.validate_ip_address(GivenIP), self.validate_port_number(GivenPort)]):
            tk.messagebox.showerror("Error", "All fields are required.")
            return

        # Do something with the values (e.g. print them to console)
        print("File path:", file_path)
        print("IP Address:", GivenIP)
        print("Port Number:", GivenPort)

root = tk.Tk()
app = App(master=root)
app.mainloop()
