from dataclasses import dataclass
from typing import NamedTuple

import jwt
from fastapi import Depends
from fastapi import HTTPException, status
from starlette.requests import Request as StarletteRequest


class BadCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Bad credentials"
        )


class RequiresAuthenticationException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )


class UnableCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to verify credentials",
        )


@dataclass
class JsonWebToken:
    jwt_access_token: str
    auth0_issuer_url: str = f"https://dev-jlrskhg3wg51jnwx.eu.auth0.com/"
    auth0_audience: str = "https://uniqa.at/uniqa_api"
    algorithm: str = "RS256"
    jwks_uri: str = f"{auth0_issuer_url}.well-known/jwks.json"

    def validate(self):
        try:
            jwks_client = jwt.PyJWKClient(self.jwks_uri)
            jwt_signing_key = jwks_client.get_signing_key_from_jwt(
                self.jwt_access_token
            ).key
            payload = jwt.decode(
                self.jwt_access_token,
                jwt_signing_key,
                algorithms=self.algorithm,
                audience=self.auth0_audience,
                issuer=self.auth0_issuer_url,
            )
        except jwt.exceptions.PyJWKClientError:
            raise UnableCredentialsException
        except jwt.exceptions.InvalidTokenError:
            raise BadCredentialsException
        return payload


class AuthorizationHeaderElements(NamedTuple):
    authorization_scheme: str
    bearer_token: str
    are_valid: bool


def get_bearer_token(request: StarletteRequest) -> str:
    authorization_header = request.headers.get("Authorization")
    if authorization_header:
        authorization_header_elements = get_authorization_header_elements(authorization_header)
        if authorization_header_elements.are_valid:
            return authorization_header_elements.bearer_token
        else:
            raise BadCredentialsException
    else:
        raise RequiresAuthenticationException


def get_authorization_header_elements(authorization_header: str, ) -> AuthorizationHeaderElements:
    try:
        authorization_scheme, bearer_token = authorization_header.split()
    except ValueError:
        raise BadCredentialsException
    else:
        valid = authorization_scheme.lower() == "bearer" and bool(bearer_token.strip())
        return AuthorizationHeaderElements(authorization_scheme, bearer_token, valid)


def validate_token(token: str = Depends(get_bearer_token)):
    return JsonWebToken(token).validate()
