import os
import time
import traceback

from loguru import logger
from openai import OpenAI


class LLMModel(object):
    def __init__(self, api_key: str,  model: str, model_params: dict[str, float | int], api_base: str = ''):
        super(LLMModel, self).__init__()
        self.api_key = api_key
        self.api_base = api_base
        self.model = model
        self.model_params = model_params
        _p = {
            "api_key": api_key
        }
        if api_base:
            _p["base_url"] = api_base
        self.client = OpenAI(
            **_p
        )

    def ask_question(self, system_prompt: str, user_prompt: str) -> str:
        try:
            start = time.time()
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                stream=False,
                **self.model_params
            )
            logger.info(f"llm api call cost {time.time() - start} seconds")
            result = completion.choices[0].message.content
            return result
        except Exception as e:
            logger.error(traceback.format_exc())
            return None


def _fetch_os_env(name: str, default: str | None = None) -> str:
    if name in os.environ:
        return os.environ.get(name)
    if default is not None:
        return default
    else:
        logger.error(
            f"Please make sure {name} has been correctly set as ENV variable")


def create_llm_model(model, model_params) -> LLMModel:
    return LLMModel(_fetch_os_env("LLM_API_KEY"),
                    model,
                    model_params,
                    _fetch_os_env("LLM_API_BASE"))
