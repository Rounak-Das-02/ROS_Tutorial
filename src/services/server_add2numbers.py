#!/usr/bin/env python3
import rospy
from testing.srv import AddTwoInts
from testing.srv import AddTwoIntsRequest
from testing.srv import AddTwoIntsResponse

def add_two_ints(request):
    print("Returning : " , (request.x + request.y))
    return AddTwoIntsResponse(request.x + request.y)

def adding_server():
    rospy.init_node("server", anonymous = True)
    server = rospy.Service("add_two_integers", AddTwoInts, add_two_ints)
    print("Ready to Add two Numbers")
    rospy.spin()

if __name__ == "__main__":
    adding_server()

