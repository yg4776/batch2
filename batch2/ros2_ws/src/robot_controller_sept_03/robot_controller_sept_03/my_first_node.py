#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

class mammal():
    def __init__(self, mammalName):
        print(mammalName, 'is a warm blooded animal')
class dog(mammal):
    def __init__(self):
        super().__init('dog')
        print('dog has 4 legs')

class MyNode(Node):
    def __init__(self):


def main(args = None):
    rclpy.init(args = args)


    rclpy.shutdown()

if __name__ == '__main__':
    main()