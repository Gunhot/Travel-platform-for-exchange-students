from rest_framework import generics
from trip.models import trip
from trip.serializers import *
from rest_framework.response import Response
from rest_framework import status

class TripList(generics.ListCreateAPIView):
    queryset = trip.objects.all()
    serializer_class = TripPostSerializer
    def get(self, request, *args, **kwargs):
        region = request.query_params.get('region', '')  # 기본값으로 빈 문자열을 설정
        period = request.query_params.get('period', '')  # 기본값으로 빈 문자열을 설정
        theme = request.query_params.get('theme', '')
        print(region, period, theme)
        try:
            if region != "" and period != "" and theme != "":
                trips = trip.objects.filter(region=region, period=period, theme=theme)
            elif region == "" and period != "" and theme != "":
                trips = trip.objects.filter(period=period, theme=theme)
            elif region != "" and period == "" and theme != "":
                trips = trip.objects.filter(region=region, theme=theme)
            elif region != "" and period != "" and theme == "":
                trips = trip.objects.filter(region=region, period=period)
            elif region != "" and period == "" and theme == "":
                trips = trip.objects.filter(region=region)
            elif region == "" and period != "" and theme == "":
                trips = trip.objects.filter(period=period)
            elif region == "" and period == "" and theme != "":
                trips = trip.objects.filter(theme=theme)
            elif region == "" and period == "" and theme == "":
                trips = trip.objects.all()
        except Exception as e:
            return Response({'message': 'No trip exists that meets the criteria'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TripGetSerializer(trips, many=True)

        # 시리얼라이즈된 정보를 응답으로 반환합니다.
        return Response(serializer.data, status=status.HTTP_200_OK)

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = trip.objects.all()
    serializer_class = TripGetSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # print(instance)
        serializer = TripGetSerializer(instance)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = TripPostSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)