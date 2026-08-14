import tkinter as tk
from tkinter import ttk
import psutil


class ResourceWidget(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("System Resource Widget")
        self.geometry("300x150")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.overrideredirect(True)

        self.bg = "#171717"
        self.fg = "#F2F2F2"
        self.muted = "#B8B8B8"

        self.configure(bg=self.bg)

        self._drag_x = 0
        self._drag_y = 0

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "CPU.Horizontal.TProgressbar",
            troughcolor="#303030",
            background="#5DADE2",
            bordercolor="#303030",
            lightcolor="#5DADE2",
            darkcolor="#5DADE2",
        )
        style.configure(
            "RAM.Horizontal.TProgressbar",
            troughcolor="#303030",
            background="#58D68D",
            bordercolor="#303030",
            lightcolor="#58D68D",
            darkcolor="#58D68D",
        )

        header = tk.Frame(self, bg=self.bg)
        header.pack(fill="x", padx=10, pady=(8, 4))

        title = tk.Label(
            header,
            text="SYSTEM MONITOR",
            bg=self.bg,
            fg=self.fg,
            font=("Segoe UI Semibold", 10),
        )
        title.pack(side="left")

        close_btn = tk.Label(
            header,
            text="✕",
            bg=self.bg,
            fg=self.muted,
            font=("Segoe UI", 10),
            cursor="hand2",
        )
        close_btn.pack(side="right")
        close_btn.bind("<Button-1>", lambda e: self.destroy())

        self._bind_drag(self)
        self._bind_drag(header)
        self._bind_drag(title)

        cpu_frame = tk.Frame(self, bg=self.bg)
        cpu_frame.pack(fill="x", padx=12, pady=(4, 6))

        self.cpu_label = tk.Label(
            cpu_frame,
            text="CPU   0%",
            bg=self.bg,
            fg=self.fg,
            anchor="w",
            font=("Segoe UI", 10),
        )
        self.cpu_label.pack(fill="x")

        self.cpu_bar = ttk.Progressbar(
            cpu_frame,
            style="CPU.Horizontal.TProgressbar",
            orient="horizontal",
            mode="determinate",
            maximum=100,
        )
        self.cpu_bar.pack(fill="x", pady=(3, 0))

        ram_frame = tk.Frame(self, bg=self.bg)
        ram_frame.pack(fill="x", padx=12, pady=(4, 6))

        self.ram_label = tk.Label(
            ram_frame,
            text="RAM   0%",
            bg=self.bg,
            fg=self.fg,
            anchor="w",
            font=("Segoe UI", 10),
        )
        self.ram_label.pack(fill="x")

        self.ram_bar = ttk.Progressbar(
            ram_frame,
            style="RAM.Horizontal.TProgressbar",
            orient="horizontal",
            mode="determinate",
            maximum=100,
        )
        self.ram_bar.pack(fill="x", pady=(3, 0))

        self.status_label = tk.Label(
            self,
            text="",
            bg=self.bg,
            fg=self.muted,
            font=("Segoe UI", 8),
            anchor="w",
        )
        self.status_label.pack(fill="x", padx=12, pady=(0, 8))

        psutil.cpu_percent(interval=None)
        self.update_stats()

    def _bind_drag(self, widget):
        widget.bind("<ButtonPress-1>", self.start_drag)
        widget.bind("<B1-Motion>", self.do_drag)

    def start_drag(self, event):
        self._drag_x = event.x_root - self.winfo_x()
        self._drag_y = event.y_root - self.winfo_y()

    def do_drag(self, event):
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y
        self.geometry(f"+{x}+{y}")

    def update_stats(self):
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory()

        self.cpu_bar["value"] = cpu
        self.ram_bar["value"] = ram.percent

        self.cpu_label.config(text=f"CPU   {cpu:5.1f}%")
        self.ram_label.config(
            text=f"RAM   {ram.percent:5.1f}%   ({ram.used / (1024**3):.1f} / {ram.total / (1024**3):.1f} GB)"
        )

        self.status_label.config(text="Güncelleme: 1 saniye  •  Sürükleyerek taşıyabilirsiniz")
        self.after(1000, self.update_stats)


if __name__ == "__main__":
    app = ResourceWidget()
    app.mainloop()
