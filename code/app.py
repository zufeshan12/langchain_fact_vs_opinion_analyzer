from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch
from langchain.schema.runnable import RunnableSequence,RunnableLambda,RunnablePassthrough
from ddgs import DDGS
import streamlit as st
from InformationClassifier import InfoClassifier
from dotenv import load_dotenv

# load environment variables
load_dotenv()
# create model
model = ChatOpenAI(name="gpt-4o")
# define feedback output parser
parser = PydanticOutputParser(pydantic_object=InfoClassifier)
# define final output parser
str_parser = StrOutputParser()

# UI components
st.header("Fact Vs Opinion Analyzer")
#initialize session state for text input
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
input_statement = st.text_input(label="Write a statement",
                                key="input_text",value=st.session_state.input_text)

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://images.unsplash.com/photo-1710162734135-8dc148f53abe");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

if st.button("Submit"):
    if input_statement:

        # load prompt using predefined prompt template
        prompt_path = 'prompt_template.json'
        prompt = load_prompt(prompt_path)
        partial_prompt = prompt.partial(format_instruction=parser.get_format_instructions())

        # load output prompts using predefined output templates
        prompt_path_fact = 'prompt_template_fact.json'
        prompt_fact = load_prompt(prompt_path_fact)

        prompt_path_opinion = 'prompt_template_opinion.json'
        prompt_opinion = load_prompt(prompt_path_opinion)

        prompt_path_amb = 'prompt_template_amb.json'
        prompt_amb = load_prompt(prompt_path_amb)

        # function to fetch supporting evidence for a factual claim
        def fetch_evidence(statement: str, max_results: int = 3):
            """Fetch supporting evidence for a fact-like statement using DuckDuckGo."""
            with DDGS() as ddgs:
                results = [r for r in ddgs.text(statement, max_results=max_results)]
            return [
                {
                    "title": r["title"],
                    "snippet": r["body"],
                    "url": r["href"]
                } for r in results
            ]


        # fill in the partial information in prompt_fact
        evidence = fetch_evidence(statement=input_statement)
        final_prompt_fact = prompt_fact.partial(evidence=evidence)
        
        # create chain to get classifier output
        classifier_chain = partial_prompt | model | parser

        #input_passthrough = RunnablePassthrough(input_statement)
        #fetch_evidence_lambda = RunnableLambda(fetch_evidence)
        
        # create branching chains based on classifier output
        branch_chain = RunnableBranch(
            (lambda x:x.classifier_output == 'fact', final_prompt_fact | model | str_parser),
            (lambda x:x.classifier_output=='opinion',prompt_opinion | model | str_parser),
            (lambda x:x.classifier_output=='ambiguous', prompt_amb | model | str_parser),
            lambda x: "Could not classify the statement")

        # create main chain and invoke it with input
        chain = classifier_chain | branch_chain 
        #chain = RunnableLambda(fetch_evidence) #| prompt_fact #| model | str_parser
        result = chain.invoke({'statement':input_statement})

        st.write(result)

# Callback function to clear the text area
def clear_text_input():
    st.session_state.input_text = ""
# clear text input on button click
st.button('Clear',on_click=clear_text_input)


