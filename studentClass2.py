import numpy as np

class Student():
    def __init__(self, n_questions, c_number, theta_f=None):
        self.n_questions = n_questions
        self.theta_f = theta_f
        self.c_number = c_number

    def generate_theta(self):
       if self.theta_f:
            not none, pass
        else:
            self.theta_dict = {i:np.random.uniform(self.c_number) for i in range (self.c_number)}
            
    def generateAnswers(self):
    i = 1
    j = 1
    k = 1
    answers_3d = []
    for i in range(self.n_questions - 1):
        answers_2d = []
        for j in range(self.c_number):
            answers_1d = []
            for k in range(self.c_number):
                x = random.randint(0,1)
                answers_1d.append(x)
            else:
                answers_2d.append(answers_1d)
        else:
            answers_3d.append(answers_2d)
    return answers_3d
