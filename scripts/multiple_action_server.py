#!/usr/bin/env python
# Copyright (c) 2020 Lucas Walter
# Demonstrate an action server that can handle multiple goals of the same type simultaneously

import rospy

from actionlib import ActionServer
from actionlib.server_goal_handle import ServerGoalHandle
from actionlib_msgs.msg import GoalID, GoalStatus
from actionlib.msg import TwoIntsAction, TwoIntsActionFeedback, TwoIntsActionGoal
from actionlib.msg import TwoIntsActionResult, TwoIntsGoal, TwoIntsResult


class MultipleActionServer(object):
    def __init__(self):
        self.goals = []
        self.action_server = ActionServer("multi", TwoIntsAction,
                                          self.goal_callback, self.cancel_callback,
                                          auto_start=False)
        self.update_timer = rospy.Timer(rospy.Duration(0.1), self.update)
        self.action_server.start()

    def goal_callback(self, goal):
        rospy.loginfo('new goal {}'.format(goal))
        self.goals.append(goal)

    def cancel_callback(self, goal):
        rospy.loginfo('cancel {}'.format(goal))

    def update(self, event):
        for goal in self.goals:
            pass


if __name__ == '__main__':
    rospy.init_node('multiple_action_server')
    multiple_action_server = MultipleActionServer()
    rospy.spin()
