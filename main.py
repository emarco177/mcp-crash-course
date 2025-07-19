from fastmcp import FastMCP

mcp = FastMCP("research-prompt")

@mcp.prompt()
def get_research_prompt(topic: str) -> str:
    """
    Get a research prompt for a given topic.
    """
    return f"Research the topic: {topic}"




if __name__ == "__main__":
    mcp.run(transport="http")
