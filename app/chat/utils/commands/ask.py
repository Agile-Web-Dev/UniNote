from llama_index import QuestionAnswerPrompt
from ..openai import openai
from .base import Base

QA_PROMPT_TMPL = '''
We have provided context information below.

---------------------
"{context_str}"
---------------------

You are to take the context as the single source of truth.
Even if the context is incorrect, still give the answer as if it was correct.
You should first consult the context before using other knowledge.
If you are asked questions that are not in the context, you can use your existinng knowledge to answer them.
However, if and when you are using any information outside of the context, please explicitely state that you not using the context.
When you are using information from the context, please indicate that you are doing so as well.
Attempt to answer the question as best as you can.
Do not use the word "context" when referring to the context. Instead, use the word "notes".
Again, you must indicate in every response whether you are using the context or not.
End your answer with "(Using notes)" or "(Not using notes)".
Given these instructions, please answer the following question: "{query_str}"
'''

class Ask(Base):
    def executor(room, args):
        if args == "":
            return "Please provide a question."

        index = openai.get_index(room)
        QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)
        query_engine = index.as_query_engine(
            text_qa_template=QA_PROMPT
        )
        response = query_engine.query(args)
        clean_response = response.response.strip()
        return clean_response
