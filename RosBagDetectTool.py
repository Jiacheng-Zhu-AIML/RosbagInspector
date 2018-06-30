import rosbag

bag_name = '2018-06-05_03'
bag_dir = '../rosbages/' + bag_name + '.bag'
bag = rosbag.Bag(bag_dir)

file = open('rosbag_detect_result.txt','w')

print bag

bag_dir = dir(bag)

topic_list = []

for topic, msg, time in bag.read_messages():

    if topic not in topic_list:
        topic_list.append(topic)

#for one in topic_list:
#    print one

default_dir_list = ['__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__getattribute__',
                    '__getstate__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__',
                    '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__',
                    '__str__', '__subclasshook__', '_check_types', '_connection_header', '_full_text',
                    '_get_types', '_has_header', '_md5sum', '_slot_types', '_spec', '_type', 'deserialize',
                    'deserialize_numpy', 'serialize', 'serialize_numpy', '__abs__', '__add__',
                    '__bool__', '__class__', '__cmp__', '__delattr__', '__div__', '__divmod__', '__doc__',
                    '__eq__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getstate__',
                    '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__mod__', '__module__',
                    '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__radd__', '__reduce__',
                    '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setstate__', '__sizeof__',
                    '__slots__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '_slot_types',
                    'canon', 'from_sec', 'is_zero', 'set', 'to_nsec', 'to_sec','ADD', 'ARROW', 'CUBE',
                    'CUBE_LIST', 'CYLINDER', 'DELETE', 'DELETEALL', 'LINE_LIST', 'LINE_STRIP', 'MESH_RESOURCE',
                    'MODIFY', 'POINTS', 'SPHERE', 'SPHERE_LIST', 'TEXT_VIEW_FACING', 'TRIANGLE_LIST',
                    '__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__getattribute__',
                    '__getstate__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__',
                    '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__',
                    '__str__', '__subclasshook__', '_check_types', '_connection_header', '_full_text',
                    '_get_types', '_has_header', '_md5sum', '_slot_types', '_spec', '_type',
                    'deserialize', 'deserialize_numpy', 'lifetime','to_time',
                    'serialize', 'serialize_numpy', 'text', 'type']


for topic in topic_list:
    for topic, msg, time in bag.read_messages(topic):

        print 'topic =', str(topic)
        file.write(str(topic))
        print 'msg =', str(msg)
        file.write(str(msg))



        break
        queue_list = ['msg']
        result_list = []

        while queue_list:

            now_path = queue_list[0]
            del queue_list[0]
            now_result = eval(now_path)

            print ''
            print 'now_path = ', now_path
            print 'now_result =', now_result
            print 'queue_list =', queue_list
            print 'result_list =', result_list
            print ''

            if type(now_result) in end_type_list:
                '''
                if this object is a result[float, bool, int, str, chr], add this path to result
                '''
                result_list.append(now_path)
                # break
            elif type(now_result) == type([1, 2]) and len(now_result) > 0:
                '''
                if this object is a non empty list, add new path to queue
                '''
                for i in range(len(now_result)):
                    temp = now_path + '[' + str(i) + ']'
                    queue_list.append(temp)
            elif type(now_result) == type([]) and len(now_result) == 0:
                '''
                if this object is an empty list, add this path to result
                '''
                result_list.append(now_path)
            else:
                '''
                if this object is just an object, find its attributes, add new path to queue
                '''
                temp_next_atbt_list = dir(now_result)
                for one in temp_next_atbt_list:
                    if one not in default_dir_list and not one[0] == '_' and one[0].islower():
                        temp = now_path + '.' + one
                        queue_list.append(temp)

        break

file.close()