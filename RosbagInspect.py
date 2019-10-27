import rosbag
import sys
import tqdm


if __name__ == '__main__':
	command_list = sys.argv
	if len(command_list) == 1:
		print ('Please input the address to the rosbag!')
		exit()
	elif len(command_list) ==2:
		rosbag_address = command_list[1]
		print ("The action is 'general' as default, please select 'general' or 'detailed'.")
		action = 'general'
		splited = rosbag_address.split('/')
		result_name = splited[-1] + '.txt'
		print ("Please input the result name(e.g. result.txt) of inspection, the name is " + result_name + " as default")
	else:
		rosbag_address = command_list[1]
		action = command_list[2]
		result_name = command_list[3] + '.txt'
	
	print (rosbag_address, action, result_name)

	

	bag = rosbag.Bag(rosbag_address)

	if action == 'general':
		sys.stdout = open(result_name, 'w')
		print bag
		exit()

	file = open(result_name, 'w')

	topic_list = []

	for topic, msg, time in bag.read_messages():
		if topic not in topic_list:
			topic_list.append(topic)
	

	for topic in topic_list:
		print (topic)
		for topic, msg, time in bag.read_messages(topic):
			# print ('topic =', str(topic))
			file.write(str(topic))
			# print ('msg =', str(msg))
			file.write(str(msg))
			break
	file.close()
	
