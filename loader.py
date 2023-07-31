from langchain.llms.fake import FakeListLLM
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.llms import OpenAI
from langchain import LLMChain
from langchain import HuggingFaceHub


class ModelFake:
    def __init__(self):
        self.llm = FakeListLLM(
            responses=[
                "Action: Give the data",
                "Final Answer: First we prepare the data.",
            ]
        )

    def generate(self, text: str) -> str:
        return self.llm(text)


class ModelOpenAI:
    def __init__(self):
        self.llm = OpenAI(
            openai_api_key="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"
        )

    def generate(self, text: str) -> str:
        template = """Question: {question}

        Answer: Let's think step by step."""

        prompt = PromptTemplate(template=template, input_variables=["question"])

        chain = LLMChain(prompt=prompt, llm=self.llm)
        return chain.run(text)


class HFStarchat:
    def __init__(self):
        model = "HuggingFaceH4/starchat-beta"

        self.llm = HuggingFaceHub(
            repo_id=model,
            huggingfacehub_api_token="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",
            model_kwargs={
                "min_length": 30,
                "max_new_tokens": 256,
                "do_sample": True,
                "temperature": 0.2,
                "top_k": 50,
                "top_p": 0.95,
                "eos_token_id": 49155,
            },
        )

    def generate(self, text: str) -> str:
        template = "<|system|>\n<|end|>\n<|user|>\n{myprompt}<|end|>\n<|assistant|>"

        prompt = PromptTemplate(template=template, input_variables=["myprompt"])
        chain = LLMChain(prompt=prompt, llm=self.llm)
        reply = chain.run(text)
        return reply.partition("<|end|>")[0]


class HFStarchat:
    def __init__(self):
        model = "HuggingFaceH4/starchat-beta"

        self.llm = HuggingFaceHub(
            repo_id=model,
            huggingfacehub_api_token="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",
            model_kwargs={
                "min_length": 30,
                "max_new_tokens": 256,
                "do_sample": True,
                "temperature": 0.2,
                "top_k": 50,
                "top_p": 0.95,
                "eos_token_id": 49155,
            },
        )

    def generate(self, text: str) -> str:
        template = "<|system|>\n<|end|>\n<|user|>\n{myprompt}<|end|>\n<|assistant|>"

        prompt = PromptTemplate(template=template, input_variables=["myprompt"])
        chain = LLMChain(prompt=prompt, llm=self.llm)
        reply = chain.run(text)
        return reply.partition("<|end|>")[0]