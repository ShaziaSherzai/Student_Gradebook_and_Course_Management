from Assessment import Assessment

class Quiz(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        return f"Quiz: {self.title} - max_score: {self.max_score}"

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 90:
            return "Excellent quiz result!"
        elif percentage >= 80:
            return "Great quiz result!"
        elif percentage >= 70:
            return "Good quiz result!"
        elif percentage >= 55:
            return "Keep practicing!"
        else:
            return "You need more practicing!"
