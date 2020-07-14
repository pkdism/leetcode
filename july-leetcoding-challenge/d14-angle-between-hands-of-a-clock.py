"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30*hour + (30/60)*minutes
        minute_angle = 6*minutes
        
        diff = abs(minute_angle - hour_angle)
        if diff > 180:
            return 360-diff
        return diff