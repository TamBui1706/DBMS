from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.DTOs.auth_dto import (
    LoginRequestDto, RegisterRequestDto, LogoutRequestDto, RefreshTokenRequestDto, AuthResponseDto, UserMeResponseDto
)

@extend_schema(request=LoginRequestDto, responses={200: AuthResponseDto})
@api_view(["POST"])
def login(request):
    serializer = LoginRequestDto(data=request.data)
    if serializer.is_valid():
        return Response({
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "refreshToken": "d98347f8-9a3b-4c2d-8e1f-6a7b8c9d0e1f",
            "tokenType": "Bearer"
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=RegisterRequestDto, responses={201: AuthResponseDto})
@api_view(["POST"])
def register(request):
    serializer = RegisterRequestDto(data=request.data)
    if serializer.is_valid():
        return Response({
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "refreshToken": "d98347f8-9a3b-4c2d-8e1f-6a7b8c9d0e1f",
            "tokenType": "Bearer"
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    parameters=[OpenApiParameter(name="allDevices", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY)],
    request=LogoutRequestDto,
    responses={200: None}
)
@api_view(["POST"])
def logout(request):
    return Response({"message": "Successfully logged out."})

@extend_schema(request=RefreshTokenRequestDto, responses={200: AuthResponseDto})
@api_view(["POST"])
def refresh_token(request):
    serializer = RefreshTokenRequestDto(data=request.data)
    if serializer.is_valid():
        return Response({
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "refreshToken": "d98347f8-9a3b-4c2d-8e1f-6a7b8c9d0e1f",
            "tokenType": "Bearer"
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    parameters=[
        OpenApiParameter(name="includeStore", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includeRole", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
    ],
    responses={200: UserMeResponseDto}
)
@api_view(["GET"])
def user_me(request):
    return Response({
        "id": "usr_998877",
        "fullName": "Sophia Munn",
        "email": "sophia@untitledui.com",
        "role": "Admin",
        "store": {"name": "My online store"}
    })
