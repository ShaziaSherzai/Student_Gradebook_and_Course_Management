import Assessment as Assessment

class Project(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        return f"Project: {self.title} - Max Score: {self.max_score}"

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 90:
            return f"Excellent project!"
        elif percentage >= 75:
            return f"Good project!"
        else :
            return f"Project needs improvement!"