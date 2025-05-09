"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import Union

from .. import DevopnessBaseService, DevopnessResponse
from ..models import Role, RoleUpdate, RoleUpdatePlain


class RolesApiService(DevopnessBaseService):
    """
    RolesApiService - Auto Generated
    """

    async def delete_role(
        self,
        role_id: int,
    ) -> DevopnessResponse[None]:
        """
        Delete a given role

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/roles/{role_id}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = await self._delete(endpoint)

        return DevopnessResponse(response, None)

    def delete_role_sync(
        self,
        role_id: int,
    ) -> DevopnessResponse[None]:
        """
        Delete a given role

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/roles/{role_id}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = self._delete_sync(endpoint)

        return DevopnessResponse(response, None)

    async def get_role(
        self,
        role_id: int,
    ) -> DevopnessResponse[Role]:
        """
        Get a role by ID

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/roles/{role_id}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = await self._get(endpoint)

        return DevopnessResponse(response, Role)

    def get_role_sync(
        self,
        role_id: int,
    ) -> DevopnessResponse[Role]:
        """
        Get a role by ID

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/roles/{role_id}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = self._get_sync(endpoint)

        return DevopnessResponse(response, Role)

    async def update_role(
        self,
        role_id: int,
        role_update: Union[
            RoleUpdate,
            RoleUpdatePlain,
        ],
    ) -> DevopnessResponse[None]:
        """
        Update an existing role

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/roles/{role_id}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = await self._put(endpoint, role_update)

        return DevopnessResponse(response, None)

    def update_role_sync(
        self,
        role_id: int,
        role_update: Union[
            RoleUpdate,
            RoleUpdatePlain,
        ],
    ) -> DevopnessResponse[None]:
        """
        Update an existing role

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/roles/{role_id}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = self._put_sync(endpoint, role_update)

        return DevopnessResponse(response, None)
