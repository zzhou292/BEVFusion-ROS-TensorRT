from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	
	node = Node(
		package="bevfusion",  
		executable="bevfusion_node",  
		name='bevfusion_node',        
		
		parameters=[
			{'model_name': 'resnet50'},
			{'precision' : 'int16'}
		]
	)

    # rviz_node = Node(
    #         package='rviz2',
    #         namespace='',
    #         executable='rviz2',
    #         name='rviz2',
    #         arguments='-d src/BEVFusion-ROS-TensorRT/launch/view.rviz'
	# )

	return LaunchDescription([
		node,
		# rviz_node
	])
