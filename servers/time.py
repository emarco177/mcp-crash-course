from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastmcp import FastMCP

app = FastAPI()

class LocationRequest(BaseModel):
    timezone: str

@app.post("/time")
async def get_time(location_req: LocationRequest):
    try:
        # Get the time in the requested timezone
        current_time = datetime.now(ZoneInfo(location_req.timezone))
        
        # Format the time for response
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        
        return {
            "timezone": location_req.timezone,
            "current_time": formatted_time
        }
    except ZoneInfoNotFoundError:
        raise HTTPException(
            status_code=400, 
            detail=f"Unknown timezone: {location_req.timezone}. Please use a valid timezone from the IANA Time Zone Database."
        )


# Create an MCP server from your FastAPI app
mcp = FastMCP.from_fastapi(app=app)

if __name__ == "__main__":
    mcp.run()  # Start the MCP server