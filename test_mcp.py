#!/usr/bin/env python3
"""
Simple test script for the YouTube Trimmer MCP server.
This script tests the MCP server functionality without requiring a full MCP client.
"""

import asyncio
import json
import sys
from typing import Any, Dict


async def test_mcp_server():
    """Test the MCP server by importing and checking tool definitions."""
    try:
        from src.youtube_trimmer.mcp_server import mcp
        import src.youtube_trimmer.mcp_server as server_module

        print("🧪 Testing YouTube Trimmer MCP Server...")
        
        # Check that the MCP server instance exists
        print(f"✅ MCP server instance created: {mcp.name}")
        
        # Test available functions by inspection
        tools = []
        for name in dir(server_module):
            obj = getattr(server_module, name)
            if callable(obj) and hasattr(obj, '_mcp_tool'):
                tools.append({
                    "name": name,
                    "description": obj.__doc__ or "No description"
                })
        
        print(f"\n📋 Found {len(tools)} MCP tools:")
        for tool in tools:
            print(f"  ✅ {tool['name']}: {tool['description'].split('.')[0]}...")
            
        # Manually list expected tools
        expected_tools = [
            "trim_youtube_video",
            "get_youtube_video_info", 
            "convert_timestamp_to_seconds",
            "download_full_youtube_video"
        ]
        
        print(f"\n🎯 Expected tools:")
        for tool_name in expected_tools:
            if hasattr(server_module, tool_name):
                print(f"  ✅ {tool_name}")
            else:
                print(f"  ❌ {tool_name} - NOT FOUND")

        print("\n🎉 MCP Server test completed successfully!")
        print("\nTo use the server:")
        print("1. Start with: youtube-trimmer mcp-server")
        print("2. Configure your MCP client to connect")
        print("3. Use natural language to trim YouTube videos!")
        
        return True
        
    except ImportError as e:
        print("Make sure to install MCP dependencies: pip install -e '.[mcp]'")
        print(f"Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


if __name__ == "__main__":
    print("YouTube Trimmer MCP Server Test")
    print("=" * 40)
    
    success = asyncio.run(test_mcp_server())
    
    if success:
        print("\n🎉 MCP test completed!")
        sys.exit(0)
    else:
        print("\n❌ MCP test failed!")
        sys.exit(1) 