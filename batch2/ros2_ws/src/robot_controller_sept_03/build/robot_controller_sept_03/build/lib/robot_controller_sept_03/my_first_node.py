#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self, varr1):
        super().__init('first node')
        self.get_logger().info("hello from ROS2")


def main(args = None):
    rclpy.init(args = args)
    
    
    node = MyNode('Batch2')
    rclpy.spin(node)


    rclpy.shutdown()

if __name__ == '__main__':
    main()