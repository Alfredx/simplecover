from pathlib import Path

from jinja2 import Template

from .model import create_llm_model


def load_template(path):
    if not Path(path).exists():
        raise FileNotFoundError(path)
    with open(path, "r") as f:
        template = Template(f.read())
        return template


def generate(cv: str, jd: str) -> str:
    model = create_llm_model("gpt-3.5-turbo", {"temperature": 0.8})
    template_path = "./simplecover/coverletter.pmpt.j2"
    system_prompt = "You are a ChatGPT assitant to help me write cover letter."
    template = load_template(template_path)
    prompt = template.render({"cv_content": cv, "jd_content": jd})
    answer = model.ask_question(system_prompt, prompt)
    return answer
