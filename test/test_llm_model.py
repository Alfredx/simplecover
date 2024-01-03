import unittest
import os
from simplecover.llm.model import _fetch_os_env, LLMModel, create_llm_model


class llm_model(unittest.TestCase):

    def test__fetch_os_env(self):
        os.environ["test_env"] = "test val"
        self.assertEqual(_fetch_os_env("test_env"), "test val")

        self.assertEqual(_fetch_os_env(
            "test_env_not_set", "default val"), "default val")

    def test_create_llm_model(self):
        model_1 = create_llm_model("test-model", {"temperature": 0.8})
        self.assertEqual(type(model_1), LLMModel)
        self.assertEqual(model_1.model, "test-model")
