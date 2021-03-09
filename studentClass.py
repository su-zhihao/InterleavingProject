import random
import numpy as np
import pandas as pd

class Student:
    """Summary of the Student class

    A student class contains learning information that worth consider for the
    question recommending model. We define sub-ability θ_ij ∈ [0, 1] to be a
    student’s ability on a question testing concept j that is preceded by a
    question testing concept i.

    We use 0 to represent a wrong answer, and 1 for the correct one

    Attributes:
        numberOfQuestions: An integer count of questions being asked
        numberOfConcepts: An integer count of concepts being tested
        theta: A dictionary represents the generating function of the student's
            subabilities on each concept. Key: An integer, value: Float lists

    Methods:
        generateTheta: Generate a theta function if we have 
        generateAnswers:
        saveData:
    """

    # Define class variable here (ex. className)

    def __init__(self, numberOfQuestions=10, numberOfConcepts=2, theta_f=None):
        """ Defining the properties of the student class """
        self.numberOfQuestions = numberOfQuestions
        self.numberOfConcepts = numberOfConcepts
        self.theta_f = theta_f

    def generateTheta(self):
        """ Randomly generate one's learning ability if not given
        Arg: A Student
        Modify: Update the subabilities dictionary if theta function is none
            ex. {0: [0.39, 0.26], 1: [0.08, 0.75]} if numberConcepts = 2
            Specifically, 0.26 means the student’s ability on a question related
            to concept 0 after completing a question related to concept 1.
        Return: None
        """
        if self.theta_f:
            pass
        else:
            key = [i for i in range(self.numberOfConcepts)]
            value = []
            for i in key:
                subAbilities = [round(random.random(), 2) for j in key]
                value.append(subAbilities)
            self.theta = dict(zip(key, value))

    def generateAnswers(self):
        """ Randomly generate the student's response based on subabilities
        Arg: A Student
        Modify: None
        Return: A 3d list (numberOfConcepts^2 * numberOfProblems) of the
            binary result of correctness. The answers describe the mapping
            from subconcepts ij to a result list of 0s and 1s that is normally
            distributed based on θ_ij. We will also save the θ_ij for each 
            subconepts following the result list
        """
        answers = []
        for i in range(self.numberOfConcepts):
            answers.append([])
            for j in range(self.numberOfConcepts):
                answers[i].append([])
                for k in range(1):
                    result = np.random.binomial(1, self.theta[i][j], 
                            self.numberOfQuestions-1)
                    answers[i][j].append(result.copy())
                    answers[i][j].append(self.theta[i][j])
        print(answers)
        return answers

    def saveData(self):
        """ Save the student's theta and response to a csv
        Arg: A Student
        Modify: In the csv file, the row represents the subablities on concept i
            while the column represents the questions being tested. Note: Since
            the first question doesn't have any previous concepts being tested.
            We will save the subabilities (theta) there.
        Return: A csv file
        """
        subablities = []
        subablities.append(list(self.theta.values()))
        result = self.generateAnswers()
        studentData = subablities + result
        df = pd.DataFrame(data = studentData)
        df.columns += 1
        # print the dataframe for debug purposes
        print(df)
        return df.to_csv('student.csv')

# Test
Patrick = Student(5,2)
print("Number of concepts: " + str(Patrick.numberOfConcepts))
print("Number of questions: " + str(Patrick.numberOfQuestions))
Patrick.generateTheta()
Patrick.saveData()
