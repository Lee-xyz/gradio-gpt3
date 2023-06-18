from enum import Enum
from gpt4free import you

class Provider(Enum):
    """An enum representing  different providers."""
    You = "you"

class Completion:
    """This class will be used for invoking the given provider"""

    @staticmethod
    def create(provider: Provider, prompt: str, **kwargs) -> str:
        """
        Invokes the given provider with given prompt and addition arguments and returns the string response

        :param provider: an enum representing the provider to use while invoking
        :param prompt: input provided by the user
        :param kwargs:  Additional keyword arguments to pass to the provider while invoking
        :return: A string representing the response from the provider
        """
        if provider == Provider.You:
            return Completion.__you_service(prompt, **kwargs)
        else:
            raise Exception("Provider does not exist. Please enter a different provider.")
        
    @staticmethod
    def __you_service(prompt: str, **kwargs) -> str:
        return you.Completion.create(prompt, **kwargs).text