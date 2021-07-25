cmake_minimum_required(VERSION 2.8.3)
project(testing)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS 
    roscpp 
    rospy 
    std_msgs 
    genmsg 
    message_generation
    )

## Declare ROS messages and services
# add_message_files(FILES Num.msg)
# add_service_files(FILES AddTwoInts.srv)

add_message_files(
    FILES 
    custom.msg
    )

add_service_files(
    FILES 
    AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)
# generate_messages()

## Declare a catkin package
catkin_package(
    INCLUDE_DIRS include
    LIBRARIES testing
    CATKIN_DEPENDS rospy roscpp std_msgs message_runtime)

# catkin_package()

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker testing_generate_messages_cpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener testing_generate_messages_cpp)


# catkin_install_python(PROGRAMS scripts/talker.py scripts/listener.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )