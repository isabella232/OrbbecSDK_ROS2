from orbbec_camera_msgs.msg import Extrinsics
from rclpy.node import Node
from rclpy.qos import qos_profile_system_default
import rclpy


class TestNode(Node):
    def __init__(self):
        super().__init__("test_node")
        self.subscription = self.create_subscription(
            Extrinsics, "/camera/extrinsics", self.callback, qos_profile_system_default
        )

    def callback(self, msg: Extrinsics):
        self.get_logger().info("=====rotation====")
        for r in msg.rotation:
            print("%s ", r)

        self.get_logger().info("=====translation====")
        for t in msg.translation:
            print("%s ", t)


def main(args=None):
    rclpy.init(args=args)
    test_node = TestNode()
    rclpy.spin(test_node)
    test_node.destry_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()