from Assessment import Assessment

class Exam(Assessment):
    def __init__(self, title, score):
        super().__init__(title, score)

    def display_info(self):
        return f"Exam: {self.title} - Max_score: {self.max_score}"

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 55:
            return "Passed exam!"
        else:
            return "Failed exam!"
        
