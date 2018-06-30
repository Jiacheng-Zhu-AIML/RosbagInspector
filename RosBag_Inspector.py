'''

Rosbag Inspector
Display all the topics and msg to give you a quick idea of one

'''
import rosbag
import sys

def Rosbag_Inspector(bag, txt_file):

    topic_list = []

    for topic, msg, time in bag.read_messages():
        if topic not in topic_list:
            topic_list.append(topic)

    for topic in topic_list:
        for topic, msg, time in bag.read_messages(topic):
            txt_file.write(str(topic))
            txt_file.write(str(msg))
            break


if __name__ == "__main__":
    rosbag_address = sys.argv[1]
    rosbag_name = sys.argv[2]
    bag = rosbag.Bag(rosbag_address)
    file = open( rosbag_name + '_result.txt','w')
    Rosbag_Inspector(bag, file)




