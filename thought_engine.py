class ThoughtEngine:
    def detect(self, shape, gaze_state):
        if shape in ["Triangle", "Rectangle"] and gaze_state == "Focused":
            return "Analytical Thinking"

        elif gaze_state == "Distracted":
            return "Confusion / Lack of Attention"

        elif shape == "Unknown Shape":
            return "Uncertain Thought"

        else:
            return "Normal Cognitive State"
