from langchain_core.prompts import PromptTemplate

template = "Ask a clarifying question for the following statement\n {statement}"


prompt_template = PromptTemplate(template=template,
                                 input_variables=['statement'])

prompt_template.save('prompt_template_amb.json')