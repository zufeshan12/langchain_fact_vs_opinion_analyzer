from langchain_core.prompts import PromptTemplate


template = "Analyze the given statement.Also analyze the provided evidence.Do not forget to display the urls in the provided evidence.Statement:{statement}\n Supporting Evidence: {evidence}"
 #"Analyze the provided evidence.Do not forget to display the urls in the provided evidence.\n evidence:{evidence}"

#"Generate a supporting evidence from DuckDuckGo app for the following statement\n {statement} using following code\n{code}"


prompt_template = PromptTemplate(template=template,
                                 input_variables=['evidence'])

prompt_template.save('prompt_template_fact.json')