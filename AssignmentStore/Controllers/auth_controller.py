from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.Services.auth_service import AuthService
from AssignmentStore.DTOs.auth_dto import (
    LoginRequestDto, RegisterRequestDto, LogoutRequestDto, RefreshTokenRequestDto, AuthResponseDto, UserMeResponseDto
)

auth_service = AuthService()

@extend_schema(tags=["Auth"], request=LoginRequestDto, responses={200: AuthResponseDto})

@api_view(["POST"])
def login(request):
    serializer = LoginRequestDto(data=request.data)
    if serializer.is_valid():
        result = auth_service.login(serializer.validated_data["email"], serializer.validated_data["password"])
        if not result:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(result)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=["Auth"], request=RegisterRequestDto, responses={201: AuthResponseDto})
@api_view(["POST"])
def register(request):
    serializer = RegisterRequestDto(data=request.data)
    if serializer.is_valid():
        result = auth_service.register(
            serializer.validated_data["fullName"],
            serializer.validated_data["email"],
            serializer.validated_data["password"]
        )
        return Response(result, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["Auth"],
    parameters=[OpenApiParameter(name="allDevices", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY)],
    request=LogoutRequestDto,
    responses={200: None}
)
@api_view(["POST"])
def logout(request):
    return Response({"message": "Successfully logged out."})

@extend_schema(tags=["Auth"], request=RefreshTokenRequestDto, responses={200: AuthResponseDto})
@api_view(["POST"])
def refresh_token(request):
    serializer = RefreshTokenRequestDto(data=request.data)
    if serializer.is_valid():
        return Response({
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.refreshed",
            "refreshToken": serializer.validated_data["refreshToken"],
            "tokenType": "Bearer"
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["Auth"],
    parameters=[
        OpenApiParameter(name="includeStore", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includeRole", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
    ],
    responses={200: UserMeResponseDto}
)

@api_view(["GET"])
def user_me(request):
    data = auth_service.get_me()
    return Response(data)

