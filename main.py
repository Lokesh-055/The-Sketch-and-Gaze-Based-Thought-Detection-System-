import tkinter as tk
from PIL import Image, ImageDraw

from sketch_recognition import SketchRecognizer
from gaze_and_face import GazeAndFace
from thought_engine import ThoughtEngine
from notifier import Notifier


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sketch & Gaze Based Thought Detection")

        # ================= CANVAS =================
        self.canvas_size = 300
        self.canvas = tk.Canvas(
            root,
            bg="white",
            width=self.canvas_size,
            height=self.canvas_size
        )
        self.canvas.pack(side=tk.LEFT)

        self.image = Image.new("RGB", (self.canvas_size, self.canvas_size), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.last_x = None
        self.last_y = None

        self.canvas.bind("<B1-Motion>", self.draw_sketch)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # ================= PANEL =================
        panel = tk.Frame(root)
        panel.pack(side=tk.RIGHT, padx=10)

        self.shape_label = tk.Label(panel, text="Shape:")
        self.shape_label.pack()

        self.gaze_label = tk.Label(panel, text="Gaze:")
        self.gaze_label.pack()

        self.thought_label = tk.Label(panel, text="Thought:")
        self.thought_label.pack(pady=10)

        tk.Button(panel, text="Predict", command=self.on_predict).pack(fill="x")
        tk.Button(panel, text="Clear", command=self.clear).pack(fill="x")
        tk.Button(panel, text="Exit", command=self.exit).pack(fill="x")

        # ================= MODULES =================
        self.sketch = SketchRecognizer()
        self.gaze = GazeAndFace()
        self.thought_engine = ThoughtEngine()

        # ================= NOTIFICATION =================
        self.user_number = "+917200460207"

        self.notifier = Notifier(
            account_sid="xxxxxxxxxxxxxxxx",
            auth_token="xxxxxxxxxxxxxx",
            from_number="+xxxxxxxxx"
        )

        # start gaze updates
        self.update_gaze()

    # ================= DRAW =================
    def draw_sketch(self, event):
        if self.last_x is not None:
            self.canvas.create_line(
                self.last_x, self.last_y,
                event.x, event.y,
                width=3
            )
            self.draw.line(
                (self.last_x, self.last_y, event.x, event.y),
                fill="black",
                width=3
            )
        self.last_x = event.x
        self.last_y = event.y

    def reset(self, _):
        self.last_x = None
        self.last_y = None

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (self.canvas_size, self.canvas_size), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.shape_label.config(text="Shape:")
        self.thought_label.config(text="Thought:")

    # ================= PREDICT =================
    def on_predict(self):
        shape, conf = self.sketch.predict(self.image)
        gaze_state = self.gaze.state
        thought = self.thought_engine.detect(shape, gaze_state)

        self.shape_label.config(text=f"Shape: {shape} ({conf:.2f})")
        self.gaze_label.config(text=f"Gaze: {gaze_state}")
        self.thought_label.config(text=f"Thought: {thought}")

        if thought == "Confusion / Lack of Attention":
            self.notifier.send(
                self.user_number,
                "You seem distracted while drawing. Please refocus on the task."
            )

    # ================= GAZE UPDATE =================
    def update_gaze(self):
        state = self.gaze.update()
        self.gaze_label.config(text=f"Gaze: {state}")
        self.root.after(30, self.update_gaze)

    # ================= EXIT =================
    def exit(self):
        self.gaze.release()
        self.root.destroy()


# ================= MAIN =================
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()

