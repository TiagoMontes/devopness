"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import List, Optional

from .. import DevopnessBaseService, DevopnessResponse
from ..models import HookRelation


class ApplicationsHooksApiService(DevopnessBaseService):
    """
    ApplicationsHooksApiService - Auto Generated
    """

    async def list_application_hooks(
        self,
        application_id: int,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[HookRelation]]:
        """
        List all hooks in an application

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = DevopnessBaseService._get_query_string(
            {
                "page": page,
                "per_page": per_page,
            }
        )

        endpoint_parts = [
            f"/applications/{application_id}/hooks",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = await self._get(endpoint)

        return DevopnessResponse(response, List[HookRelation])

    def list_application_hooks_sync(
        self,
        application_id: int,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[HookRelation]]:
        """
        List all hooks in an application

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = DevopnessBaseService._get_query_string(
            {
                "page": page,
                "per_page": per_page,
            }
        )

        endpoint_parts = [
            f"/applications/{application_id}/hooks",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = self._get_sync(endpoint)

        return DevopnessResponse(response, List[HookRelation])
