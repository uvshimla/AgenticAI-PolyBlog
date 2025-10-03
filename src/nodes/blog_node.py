
from src.states.blogstate import BlogState
from langchain_core.messages import HumanMessage,SystemMessage
from src.states.blogstate import Blog

class BlogNode:
    """
    Class to represent blog node
    """
    def __init__(self, llm):
        self.llm=llm

    def title_creating(self, state: BlogState):
        """
        Create the title for the blog
        """
        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly

                   """
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {
                'blog':{
                    'title': response.content
                }
            }
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}
    def translation(self, state: BlogState, language: str = None):
        """Translate the blog content to the given language
        """
        target_language = language or state.get('current_language', 'hindi')
        translation_prompt = """Translate the following blog content to the given language: {current_language} .
        -Maintain the original tone and formating.
        -Adapt cultural references and idioms to be appropriate for {current_language}.
        ORIGINAL CONTENT:
        {blog_content}
        """
        blog_content = state['blog']['content']
        messages=[
            HumanMessage(translation_prompt.format(current_language=target_language, blog_content=blog_content))
        ]
        translated_blog = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog": translated_blog}
    def route(self, state:BlogState):
        """Route the blog content to the specific language"""
        if state['current_language']=="hindi":
            return "hindi"
        elif state['current_language']=="french":
            return "french"
        else:
            return state['current_language']