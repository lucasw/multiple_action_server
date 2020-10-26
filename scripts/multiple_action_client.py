#!/usr/bin/env python
# Copyright (c) 2020 Lucas Walter
# Demonstrate an action client that can send multiple goals of the same type simultaneously

import rospy

from actionlib import ActionClient
# from actionlib.server_goal_handle import ServerGoalHandle
# from actionlib_msgs.msg import GoalID, GoalStatus
# from actionlib.msg import TwoIntsAction, TwoIntsActionFeedback, TwoIntsActionGoal
from actionlib.msg import TwoIntsAction, TwoIntsGoal
# from actionlib.msg import TwoIntsActionResult, TwoIntsGoal, TwoIntsResult


class MultipleActionClient(object):
    def __init__(self):
        # TODO(lucasw) make an object hold the goal and goal handle and anything else needed
        self.goal_handles = []
        self.action_client = ActionClient("multi", TwoIntsAction)

        for i in range(4):
            goal = TwoIntsGoal()
            gh = self.action_client.send_goal(goal,
                                              self.handle_transition,
                                              self.handle_feedback)
            self.goal_handles.append(gh)
            rospy.sleep(1.0)

        # self.update_timer = rospy.Timer(rospy.Duration(0.1), self.update)
        # self.action_client.start()

    def handle_transition(self, gh):
        rospy.loginfo('transition {}'.format(gh))

    def handle_feedback(self, gh, feedback):
        rospy.loginfo('feedback {} {}'.format(gh, feedback))

    def update(self, event):
        for goal in self.goals:
            pass


if __name__ == '__main__':
    rospy.init_node('multiple_action_client')
    multiple_action_client = MultipleActionClient()
    rospy.spin()
