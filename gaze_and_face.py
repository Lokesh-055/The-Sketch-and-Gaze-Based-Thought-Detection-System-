import cv2
import mediapipe as mp

class GazeAndFace:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        self.state = "Focused"

    def update(self):
        ret, frame = self.cap.read()
        if not ret:
            return self.state

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb)

        if result.multi_face_landmarks:
            self.state = "Focused"
            for face in result.multi_face_landmarks:
                for lm in face.landmark:
                    h, w, _ = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        else:
            self.state = "Distracted"

        cv2.imshow("Face & Gaze Tracking", frame)
        cv2.waitKey(1)

        return self.state

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
