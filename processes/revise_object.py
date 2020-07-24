
# first the user enters their selection
#   based on the selection and the state of the passed in object, confirmation text will be returned
# after the user confirms thier selection it will handle the indavidual result

# i think there should be one class for the actual revision/manipulation of deliveries
# and then another class that is the menu the user interacts with, that uses the revision class

from processes.input_data import Input_Delivery
class Revise_Delivery(Input_Delivery):
    def __init__(self, delivery):
        self.delivery = delivery
        self.file_list = delivery.file_list()
    
    def edit_average_speed(self):
        from utility.file import write
        # input and save average speed
        delivery.average_speed = self.average_speed()
        write(delivery.average_speed, self.file_list['average_speed'])

    def edit_distance(self):
        from utility.file import write
        # input and save distance traveled
        delivery.miles_traveled = self.distance()
        write(delivery.miles_traveled, self.file_list['miles_traveled'])

    def edit_end_time(self):
        # todo: need to make custom class to allow user to modify datetimes,date,time
        pass
    
    def edit_start_time(self):
        # todo: need to make custom class to allow user to modify datetime,date,time
        pass
