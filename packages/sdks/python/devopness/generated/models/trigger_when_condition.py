"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    List,
    Optional,
    Required,
    TypedDict,
    Union,
)

from pydantic import Field, StrictStr

from .. import DevopnessBaseModel
from .trigger_when_condition_accepted_values_inner import (
    TriggerWhenConditionAcceptedValuesInner,
    TriggerWhenConditionAcceptedValuesInnerPlain,
)
from .trigger_when_condition_type import (
    TriggerWhenConditionType,
    TriggerWhenConditionTypePlain,
)


class TriggerWhenCondition(DevopnessBaseModel):
    """
    TriggerWhenCondition

    Attributes:
        name (str, optional): Name of the condition
        type (TriggerWhenConditionType):
        path (str): A dot-notation path of the request body attribute to be used as the value to evaluate this condition.
        accepted_values (List[TriggerWhenConditionAcceptedValuesInner]): List of accepted values for this condition.
    """

    name: Optional[StrictStr] = Field(default=None, description="Name of the condition")
    type: TriggerWhenConditionType
    path: StrictStr = Field(
        description="A dot-notation path of the request body attribute to be used as the value to evaluate this condition."
    )
    accepted_values: List[TriggerWhenConditionAcceptedValuesInner] = Field(
        description="List of accepted values for this condition."
    )


class TriggerWhenConditionPlain(TypedDict, total=False):
    """
    Plain version of TriggerWhenCondition.
    """

    name: Optional[str]
    type: Required[
        Union[
            TriggerWhenConditionType,
            TriggerWhenConditionTypePlain,
        ]
    ]
    path: Required[str]
    accepted_values: Required[
        List[
            Union[
                TriggerWhenConditionAcceptedValuesInner,
                TriggerWhenConditionAcceptedValuesInnerPlain,
            ]
        ]
    ]
