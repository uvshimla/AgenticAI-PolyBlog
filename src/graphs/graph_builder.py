from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph=StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blogs based on topic
        """
        self.blog_node_obj = BlogNode(self.llm)
        # Create Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creating)
        self.graph.add_node("content_creation", self.blog_node_obj.content_generation)

        # Add Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_creation")
        self.graph.add_edge("content_creation", END)

        return self.graph

    
    def build_language_graph(self):
        """
        Build a graph to blog generation with input topic and language
        """
        self.blog_node_obj = BlogNode(self.llm)
        # Create Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creating)
        self.graph.add_node("content_creation", self.blog_node_obj.content_generation)
        self.graph.add_node("hindi_translation", lambda state: self.blog_node_obj.translation(state, language="hindi"))
        self.graph.add_node("french_translation", lambda state: self.blog_node_obj.translation(state, language="french"))

        # Add Edges and conditional edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_creation")
        self.graph.add_conditional_edges(
            "content_creation",
            self.blog_node_obj.route,
            {
                "hindi": "hindi_translation",
                "french": "french_translation",
            }
        )
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)

        return self.graph
    
    def setup_graph(self, usecase):
        if usecase=="topic":
            self.build_topic_graph()
        elif usecase=="language":
            self.build_language_graph()

        return self.graph.compile()


## Below code is for the langsmith langgraph studio
llm=GroqLLM().get_llm()

## get the graph
graph_builder=GraphBuilder(llm)
graph=graph_builder.build_topic_graph().compile()