from langchain_core.prompts import PromptTemplate

template = "Generate a balanced counter-opinion for the following statement:\n{statement}"


prompt_template = PromptTemplate(template=template,
                                 input_variables=['statement'])

prompt_template.save('prompt_template_opinion.json')