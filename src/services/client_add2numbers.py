#!/usr/bin/env python3
import rospy
import sys
from testing.srv import AddTwoInts
from testing.srv import AddTwoIntsRequest
from testing.srv import AddTwoIntsResponse

def input_two_numbers():
    x = int(input("Enter First Number : "))
    y = int(input("Enter Second Number : "))
    return x,y

def client_add(x, y):
    rospy.wait_for_service("add_two_integers")
    try:
        add = rospy.ServiceProxy("add_two_integers", AddTwoInts)
        response = add(x, y)
        return response
    except rospy.ServiceException as e:
        print("[ERROR] Service Call FAILED")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        x, y = input_two_numbers()
    
    print("Requesting Sum of %s and %s" %(x,y))
    print("Fetching the Answer ...")
    print(client_add(x,y))

