from dataclasses import field, dataclass, fields


@dataclass
class BaseSchema:

    attrs: dict = field(default_factory=dict, metadata={"type": "Attributes"})

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )
