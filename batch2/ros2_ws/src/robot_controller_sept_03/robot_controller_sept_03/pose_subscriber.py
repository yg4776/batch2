#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber") #node name
        self.pose_subscriber_ = self.create_subscription(Pose,"/turtle1c/pose",self.pose_callback, 10)

    def pose_callback(self,msg:Pose):
        self.get_logger().info("Draw circle node has started")


def main(args = None):
    rclpy.init(args = args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()