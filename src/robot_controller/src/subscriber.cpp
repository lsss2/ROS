#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "nav_msgs/msg/odometry.hpp" // cambiar a odometry
using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
  public:
    MinimalSubscriber()
    : Node("minimal_subscriber")
    {
      subscription_ = this->create_subscription<nav_msgs::msg::Odometry>(
      "odom", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
    }

  private:
    void topic_callback(const nav_msgs::msg::Odometry & msg) const
    {
      // Print the robot position from the Odometry message
      auto x = msg.pose.pose.position.x;
      auto y = msg.pose.pose.position.y;
      auto z = msg.pose.pose.position.z;
      RCLCPP_INFO(this->get_logger(), "I heard position: x=%.3f, y=%.3f, z=%.3f", x, y, z);
    }
    rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}
