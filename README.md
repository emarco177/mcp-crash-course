# MCP Terminal Server

A simple MCP (Model Context Protocol) server that exposes terminal commands and access to pictures.

## Setup

1. Install the required dependencies:

```bash
pip install mcp httpx
```

2. Run the server:

```bash
python server.py
```

## Usage

### With Claude Desktop

You can install this server in Claude Desktop:

```bash
mcp install server.py
```

### With MCP Inspector

Alternatively, you can test it with the MCP Inspector:

```bash
mcp dev server.py
```

## Tools and Resources

### run_command

This tool allows you to execute terminal commands and receive their output.

**Parameters:**
- `command` (string): The terminal command to execute

**Returns:**
- A dictionary containing:
  - `stdout`: Standard output from the command
  - `stderr`: Error output from the command
  - `return_code`: The command's exit code

### get_image_content

This tool retrieves the content of an image file as a base64 encoded string.

**Parameters:**
- `file_path` (string): Path to the image file. Can be a full path or just the filename (will look in Desktop/pics)

**Returns:**
- A dictionary containing:
  - `filename`: The name of the file
  - `path`: The full path to the file
  - `size_bytes`: The size of the file in bytes
  - `mime_type`: The MIME type of the image
  - `data_uri`: A data URI that can be used to display the image
  - `base64`: The base64-encoded content of the image

### pictures://{subfolder}

This resource provides access to pictures in the Desktop/pics folder.

**Parameters:**
- `subfolder` (optional string): A subfolder within the pics directory

**Returns:**
- A dictionary containing:
  - `path`: The full path to the directory
  - `pictures`: An array of picture files with metadata
  - `subdirectories`: An array of subdirectory names
  - `count`: The number of pictures found

## Security Note

This server provides direct access to terminal commands and the filesystem, which presents security risks. Use this server only in controlled environments and with trusted clients.
