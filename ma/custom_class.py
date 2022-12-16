#from rest_framework.pagination import CursorPagination
#class MyCursorPagination(CursorPagination):
#    ordering='id'


import rest_framework.pagination
class MyCursorPagination(rest_framework.pagination.CursorPagination):
    ordering='id'
