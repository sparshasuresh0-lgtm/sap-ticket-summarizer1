from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sap-ticket-assistant")


@mcp.tool()
async def summarize_ticket_tool(ticket: str):

    return {
        "summary": f"SAP issue detected for: {ticket}",
        "priority": "HIGH",
        "root_cause": "RFC timeout",
        "actions": [
            "Restart SAP Gateway",
            "Check SAP network connectivity",
            "Validate RFC destination"
        ]
    }


if __name__ == "__main__":
    print("MCP SERVER STARTED")
    mcp.run(transport="stdio")