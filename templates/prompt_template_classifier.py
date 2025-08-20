from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

template = "Classify the following statement as fact,opinion or ambiguous:\n{statement}.\n {format_instruction}"

prompt_template = PromptTemplate(template=template,
                                 input_variables=['statement','format_instruction'],
                                 #partial_variables={'format_instruction':parser.get_format_instructions()}
                                 )

prompt_template.save("prompt_template.json")