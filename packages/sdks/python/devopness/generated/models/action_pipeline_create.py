"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    List,
    Optional,
    TypedDict,
    Union,
)

from pydantic import Field, StrictInt, StrictStr

from .. import DevopnessBaseModel
from .source_type import SourceType, SourceTypePlain


class ActionPipelineCreate(DevopnessBaseModel):
    """
    ActionPipelineCreate

    Attributes:
        servers (List[int], optional): List of valid resource IDs
        source_type (SourceType, optional):
        source_ref (str, optional): A git reference pointing to a commit in a source provider repository from which the application source code will be retrieved and deployed. It can be a branch name, tag name or a specific commit hash. Must not be greater than 200 characters.
    """

    servers: Optional[List[StrictInt]] = Field(
        default=None, description="List of valid resource IDs"
    )
    source_type: Optional[SourceType] = None
    source_ref: Optional[StrictStr] = Field(
        default=None,
        description="A git reference pointing to a commit in a source provider repository from which the application source code will be retrieved and deployed. It can be a branch name, tag name or a specific commit hash. Must not be greater than 200 characters.",
    )


class ActionPipelineCreatePlain(TypedDict, total=False):
    """
    Plain version of ActionPipelineCreate.
    """

    servers: Optional[List[int]]
    source_type: Optional[
        Union[
            SourceType,
            SourceTypePlain,
        ]
    ]
    source_ref: Optional[str]
