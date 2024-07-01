from rest_framework.pagination import PageNumberPagination


class My_Pagination(PageNumberPagination):
    page_size = 10