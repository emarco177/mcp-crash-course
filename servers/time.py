from fastmcp import FastMCP
import datetime
import pytz
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp")
logger.setLevel(logging.INFO)
mcp = FastMCP(
    name="Current Date and Time",
    instructions="When you are asked for the current date or time, call current_datetime() and pass along an optional timezone."
)

@mcp.tool()
def current_datetime(timezone: str = "America/New_York") -> str:
    """
    Returns the current date and time as a string.
    If you are asked for the current date or time, call this function.

    Args:
        timezone: Timezone name (e.g., 'UTC', 'US/Pacific', 'Europe/London').
                  Defaults to 'America/New_York'.

    Returns:
        A formatted date and time string.
    """
    try:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
        return now.strftime("%Y-%m-%d %H:%M:%S %Z")
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'. Please use a valid timezone name."

if __name__ == "__main__":
    import asyncio
    port = os.getenv("PORT", 10000)
    logger.info(f"Running on port {port}")
    asyncio.run(
        mcp.run_sse_async(
            host="0.0.0.0",
            port=port,
            log_level="debug"
        )
    )