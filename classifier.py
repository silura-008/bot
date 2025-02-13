from typing import Dict, Text, Any, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData

from transformers import pipeline

@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.INTENT_CLASSIFIER], is_trainable=True
)
class EmotionClassifier(GraphComponent):
    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> GraphComponent:
        model_name = config.get("model_name", "SamLowe/roberta-base-go_emotions")
        return cls(model_name)

    def __init__(self, model_name: Text) -> None:
        self.model = pipeline("text-classification", model=model_name, top_k=None)

    def train(self, training_data: TrainingData) -> Resource:
        # No training required for this component
        return Resource("EmotionClassifier")

    def process_training_data(self, training_data: TrainingData) -> TrainingData:
        # No processing of training data required for this component
        return training_data

    def process(self, messages: List[Message]) -> List[Message]:
        for message in messages:
            model_outputs = self.model(message.data["text"])
            if model_outputs and isinstance(model_outputs, list) and isinstance(model_outputs[0], list):
                model_outputs = model_outputs[0]  # Extract the inner list
            
            if model_outputs:
                # print(f"model_output : {model_outputs}")
                intent_prediction = max(model_outputs, key=lambda x: x["score"])  # Find highest confidence
                # print(f"intent_prediction : {intent_prediction}")
                message.set("intent", {
                    "name": intent_prediction["label"],
                    "confidence": intent_prediction["score"]
                },add_to_output=True)
        return messages

