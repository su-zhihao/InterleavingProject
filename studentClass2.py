import numpy as np

class Student():
    def __init__(self, n_questions, c_number, theta_f=None):
        self.n_questions = n_questions
        self.theta_f = theta_f
        self.c_number = c_number

    def generate_theta(self):
        if self.theta_f:
             pass # use theta_f
        else:
            self.theta_dict = {i:np.random.uniform(self.c_number) for i in range (self.c_number)}
