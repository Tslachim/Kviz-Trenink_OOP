class Brain:

    def __init__(self, q_list):
        self.que_li = q_list
        self.que_num = 0
        self.score = 0

    def next_question(self):
        current_question = self.que_li[self.que_num]
        self.que_num += 1 
        user_answer = input(f"Otázka č. {self.que_num}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)    

    def has_question(self):
        if self.que_num < len(self.que_li):
            return True
        else:
            return False
    
    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print("Uhádli jste!")
            self.score += 1
        else:
            print("Špatná odpověď.")
        print(f"Vaše skóre je: {self.score}/{self.que_num}")