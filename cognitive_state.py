class CognitiveStateEstimator:
    def __init__(self):
        # hyperparams for rule-based scoring
        self.blink_rate_threshold = 0.5  # blinks per second -> high means tired
        self.low_confidence_threshold = 0.6

    def estimate(self, sketch_pred, gaze_feats, emotion_pred, session_stats=None):
        # sketch_pred: {'label','confidence'}
        # gaze_feats: dict with gaze_vec, ear, blink
        # emotion_pred: {'happy':0.1,'sad':0.2,...}
        score = {'focused':0, 'distracted':0, 'confused':0, 'frustrated':0}

        # sketch confidence: high confidence increases focused
        conf = sketch_pred.get('confidence', 0.0)
        if conf > 0.8:
            score['focused'] += 2
        elif conf > 0.5:
            score['focused'] += 1
        else:
            score['confused'] += 1

        # gaze: if gaze vector magnitude small -> focused, else distracted
        gv = gaze_feats.get('gaze_vec', (0,0))
        mag = (gv[0]**2 + gv[1]**2)**0.5
        if mag < 0.01:
            score['focused'] += 1
        else:
            score['distracted'] += 1

        # blink/ear: low EAR (many blinks) -> tired/frustrated
        ear = gaze_feats.get('ear', 1.0)
        if ear < 0.18:
            score['frustrated'] += 1

        # emotion preds
        angry = emotion_pred.get('angry',0)
        neutral = emotion_pred.get('neutral',0)
        happy = emotion_pred.get('happy',0)
        sad = emotion_pred.get('sad',0)
        if angry > 0.4 or sad > 0.4:
            score['frustrated'] += 2
        if neutral > 0.6:
            score['focused'] += 1
        if happy > 0.6:
            score['focused'] += 1

        # choose top
        top = max(score, key=score.get)
        return {'state': top, 'scores': score}