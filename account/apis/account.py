# from rest_framework import mixins
# from rest_framework import viewsets
#
# from ..filters import BranchFilter
# from ..models import Branch
# from ..schemas import BranchSerializer
#
#
# class ViewSetBranch(mixins.ListModelMixin,
#                     viewsets.GenericViewSet, ):
#     filter_class = BranchFilter
#
#     def get_queryset(self):
#         return Branch.objects.all()
#
#     def get_serializer_class(self):
#         return BranchSerializer
