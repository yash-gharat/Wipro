# Assignment
# TechWorld, a technology training center, wants to allocate courses for instructors.
# An instructor is identified by name, technology skills, experience and average feedback.
# An instructor is allocated a course, if he/she satisfies the below two conditions:
# eligibility criteria:
# if experience is more than 3 years, average feedback should be 4.5 or more
# if experience is 3 years or less, average feedback should be 4 or more
# he/she should posses the technology skill for the course
# Identify the class name and attributes to represent instructors. Drag and drop the chosen class name, attributes and methods into the appropriate section of the box shown below.
 
 
# calculate_avg_feedback()
# avg_feedback
# Instructor
# check_eligibility()
# allocate_course()
# __init__()
# instructor_name
# experience
# allocate_course(technology)
# technology_skill


# Class - Instructor
# attributes - instructor_name,avg_feedback,experience,technology_skill
# methods -__init__(),check_eligibility(),allocate_course(technology)

class Instructor:
    def __init__(self,instructor_name,avg_feedback,experience,technology_skills) -> None:
        self.instructor_name = instructor_name,
        self.avg_feedback = avg_feedback
        self.experience = experience
        self.technology_skills = technology_skills    
    def check_eligibility(isAvaiable):
        return isAvaiable
        # pass
    def calculate_avg_feedback():
        pass
    def allocate_course(self,technology):
        if technology in self.technology_skills:
            print(f"{self.instructor_name} is allocated for the course on {technology}.")
        else:
            print(f"{self.instructor_name} is not eligible for the course on {technology}.")
    def calculate_avg_feedback():
        pass

instructor1 = Instructor(instructor_name="John", technology_skills=["Python", "Machine Learning"], experience=4, avg_feedback=4.7)
instructor2 = Instructor(instructor_name="David", technology_skills=["Java", "App Development"], experience=2, avg_feedback=4.2)
instructor3= Instructor(instructor_name="Sam", technology_skills=["Javascript", "Web Development"], experience=2, avg_feedback=4.2)

#avaiablity

# instructor1.check_eligibility(True)

instructor1.allocate_course("Python")
instructor2.allocate_course("Java")
instructor2.allocate_course("Machine Learning")
instructor3.allocate_course("Swift")
