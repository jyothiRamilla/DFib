from rest_framework import serializers
from rest_framework import parsers, exceptions
from rest_framework.exceptions import ParseError


from . models  import emp
class empSerializer(serializers.ModelSerializer):
    class Meta:
        model =  emp
        fields='__all__'