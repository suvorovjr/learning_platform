from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer
from course.models import Course


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data['course']
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item, created = Subscription.objects.get_or_create(user=user, course=course_item)
        if created:
            message = 'Вы подписались на обновления курса'
        else:
            subs_item.delete()
            message = 'Вы отписались от обновления курса'
        return Response({"message": message})
