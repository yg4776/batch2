#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle") #node name
        self.cmd_vel_pub = self.create_publisher(Twist,"/turtle1c/cmd_vel", 10)
        self.create_timer(0.5, self.send_velocity_commands)
        self.get_logger().info("Draw circle node has started")

    def send_velocity_commands(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.2
        self.cmd_vel_pub.publish(msg)


def main(args = None):
    rclpy.init(args = args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()