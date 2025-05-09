"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import List, Optional

from .. import DevopnessBaseService, DevopnessResponse
from ..models import ActionRelation


class ProjectsActionsApiService(DevopnessBaseService):
    """
    ProjectsActionsApiService - Auto Generated
    """

    async def list_project_actions_by_resource_type(
        self,
        project_id: int,
        resource_type: str,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[ActionRelation]]:
        """
        List project actions of a resource type

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
            f"/projects/{project_id}/actions/{resource_type}",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = await self._get(endpoint)

        return DevopnessResponse(response, List[ActionRelation])

    def list_project_actions_by_resource_type_sync(
        self,
        project_id: int,
        resource_type: str,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[ActionRelation]]:
        """
        List project actions of a resource type

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
            f"/projects/{project_id}/actions/{resource_type}",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)
        response = self._get_sync(endpoint)

        return DevopnessResponse(response, List[ActionRelation])
