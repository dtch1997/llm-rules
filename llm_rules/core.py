from dataclasses import dataclass

@dataclass
class LLMRuleData:
    text: str
    label: int | None # 0 or 1

    @property
    def is_labelled(self) -> bool:
        return self.label is not None

@dataclass
class LLMRuleDataset:
    data: list[LLMRuleData]
    rule: str

    @property
    def positive_data(self) -> list[LLMRuleData]:
        return [d for d in self.data if d.label == 1]
    
    @property
    def negative_data(self) -> list[LLMRuleData]:
        return [d for d in self.data if d.label == 0]
