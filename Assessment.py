class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return ( score / self.max_score ) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 90:
            print("Excellent Performance!")
        elif percentage >= 80:
            print("Great Job!")
        elif percentage >= 70:
            print("Very Good Job!")
        elif percentage >= 55:
            print("You Passed!")
        else:
            print("You're Failed")

    def display_info(self):
        print(f"{self.title}: - Max_score: {self.max_score}")
