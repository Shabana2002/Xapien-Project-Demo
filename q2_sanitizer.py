class DataSanitizer:
    def __init__(self, data):
        self.data = data

    def to_cm(self, key, value):
        if key == "Height":
            if value < 100:
                return value * 2.54
            return value
        else:
            if value < 50:
                return value * 2.54
            return value

    def normalize(self):
        normalized = {}
        for k, v in self.data.items():
            normalized[k] = self.to_cm(k, v)

        self.data = normalized
        return normalized

    def validate(self):
        h = self.data.get("Height")
        w = self.data.get("Waist")
        c = self.data.get("Chest")

        issues = []

        if w and h and w > h:
            issues.append("Waist cannot be greater than Height")

        if c and h and c < 0.3 * h:
            issues.append("Chest is unrealistically small compared to Height")

        return issues

    def estimate_missing(self):
        h = self.data.get("Height")

        if "Arm" not in self.data and h:
            self.data["Arm"] = round(0.45 * h, 2)

        return self.data