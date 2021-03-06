import stripe
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from TheBookshelf import settings
from .models import Top_up_item, Subscription_Plan, User_profile
from .serializers import TopUpItemSerializer, SubscriptionSerializer, UserProfileSerializer


# Create your views here.

class TopUpView(ListAPIView):
    serializer_class = TopUpItemSerializer
    queryset = Top_up_item.objects.all()
    permission_classes = [AllowAny]


class SubscriptionView(ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription_Plan.objects.filter(is_featured=True)
    permission_classes = [AllowAny]


class UserProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User_profile.objects.get_or_create(plan_id=3, user_id=self.request.user.id)


@api_view(['POST'])
def cancel_plan(request):
    user_profile = User_profile.objects.get(user_id=request.user.id)
    plan_free = Subscription_Plan.objects.get(title='Free')

    user_profile.plan = plan_free
    user_profile.plan_status = user_profile.PLAN_INACTIVE
    user_profile.save()

    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.Subscription.delete(user_profile.stripe_subscription_id)
        user_profile.stripe_subscription_id = None
        user_profile.save()
    except Exception:
        return Response({'error': 'Something went wrong. Please try again'})

    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)
