# 3rd party libraries
from rest_framework import serializers
from UserActivity.user.models import User, ActivityPeriod
import pytz
from datetime import datetime
DATE_FORMAT = '%b %d %Y %H:%M%p'


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format=DATE_FORMAT)
    end_time = serializers.DateTimeField(format=DATE_FORMAT)

    class Meta:
        model = ActivityPeriod
        fields = ("start_time", "end_time", )

    # def get_start_time(self, activity):
    #     return activity.start_time
    #
    # def get_end_time(self, activity):
    #     date_ = pytz.timezone(str(activity.user.timezone_info)).localize(
    #         datetime.strptime(str(activity.end_time), '%Y-%m-%d %H:%M:%S'))
    #     return date_


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    tz = serializers.SerializerMethodField(read_only=True)
    activity_periods = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "real_name", "tz", "activity_periods")

    def get_id(self, user):
        return user.user_id

    def get_tz(self, user):
        return str(user.timezone_info)

    def get_activity_periods(self, user):
        activities = user.activityperiod_set.all()
        # if activities:
        return ActivityPeriodSerializer(user.activityperiod_set.all(), many=True).data
        # return []
