import random 

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
        generateTheta:
        generateAnswers:
        saveData:
    """

    # Define class variable here (ex. className)

    def __init__(self, numberOfQuestions, numberOfConcepts, theta=None):
        """ Defining the properties of the student class """
        self.numberOfQuestions = numberOfQuestions
        self.numberOfConcepts = numberOfConcepts
        self.theta = theta

    def generateTheta(self):
        """ Randomly generate one's learning ability if not given
        Arg: A Student
        Modify: Update dictionary of if theta function is none
            ex. {1: [0.39, 0.26], 2: [0.08, 0.75]} if numberConcepts = 2
            Specifically, 0.26 means the student’s ability on a question related
            to concept 1 after completing a question related to concept 2.
        Return: None 
        """
        if self.theta is None:
            key = [i for i in range(1,self.numberOfConcepts+1)]
            value = []
            for i in range(1,self.numberOfConcepts+1):
                subAbilities = [round(random.random(), 2) for j 
                        in range(1,self.numberOfConcepts+1)]
                value.append(subAbilities)
            self.theta = dict(zip(key, value))

    def generateAnswers(self):
        """ Randomly generate the student's response to a given problem set  
        Arg: A Student
        Modify: None
        Return: A 3d list (numberOfProblems * numberOfConcepts^2) of the binary 
            result of correctness
        """
        answers = []
        for i in range(self.numberOfQuestions):
            answers.append([])
            for j in range(self.numberOfConcepts):
                answers[i].append([])
                for k in range(self.numberOfConcepts):
                    answers[i][j].append(random.choice([0,1]))
        return answers

    def saveData(self):
    # TODO Add the student's information to a larger collector
        return

Patrick = Student(3,2)
print(Patrick.numberOfConcepts)
print(Patrick.numberOfQuestions)
Patrick.generateTheta()
print(Patrick.theta)
print(Patrick.generateAnswers())