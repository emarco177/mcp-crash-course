# MCP Crash Course 🚀
![MCP Tool Call Demo](/static/mcp-tool-call.gif)


[![Twitter Follow](https://img.shields.io/twitter/follow/EdenMarco177?style=social)](https://twitter.com/EdenMarco177)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[![udemy](https://img.shields.io/badge/MCP%20Udemy%20Course%20Coupon%20%2412.99-brightgreen)](https://www.udemy.com/course/model-context-protocol/?couponCode=OCT-2025)

Welcome to the MCP Crash Course! This repository is designed to teach you the fundamentals and advanced concepts of the Model Context Protocol (MCP) in a hands-on way.

## What is MCP? 💡

The Model Context Protocol (MCP) helps connect AI-agentic applications powered by Large Language Models (LLMs) to external tools and data sources, enabling more capable and context-aware AI systems.

## How it Works 🤔

This repository uses a unique branch-based structure for learning:

1.  **Each `project/*` branch covers a specific MCP feature or concept.**
2.  **Within each branch, commits are ordered chronologically.** Follow the commits one by one to learn the topic step-by-step.

Simply check out the branch for the topic you want to learn and walk through the commits!

## Available Topics (Branches) 📚

Here are the topics currently available:

*   `project/sse`: Learn how to implement Server-Sent Events (SSE) with MCP.
*   `project/langchain-mcp-adapters`: Explore integrating MCP with LangChain adapters.
*   `project/docker-mcp`: Understand how to containerize your MCP applications using Docker.
*   `project/prompts`: Learn how to implement and work with MCP Prompts, featuring FastMCP 2.0.

*More topics might be added, so keep an eye out!*

## Prerequisites 🛠️

Before you start, make sure you have the following installed:

*   🐍 Python (version 3.10 or higher)
*   📦 `uv` (the fast Python package installer and resolver)
*   ✨ Cursor IDE
*   ☁️ Claude Desktop

## Getting Started ▶️

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/emarco177/mcp-crash-course.git
    cd mcp-crash-course
    ```
2.  **Choose a topic and check out the branch:**
    ```bash
    # Example for the SSE topic
    git checkout project/sse
    ```
3.  **Follow the commits:** Use `git log --oneline --reverse` to see the chronological list of commits for the branch. Then, use `git checkout <commit_hash>` or your Git client to step through the history and learn.

## Contributing 🤝

Contributions are welcome! If you'd like to add a new topic or improve an existing one:

1.  Fork the repository.
2.  Create a new branch for your feature following the naming convention: `project/your-mcp-feature-name`.
3.  Make your changes, ensuring each commit represents a logical step in the learning process.
4.  Open a Pull Request against the `main` branch.

## License 📄

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Happy learning! 🎉


