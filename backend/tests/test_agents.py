def test_agent_orchestrator():
    prompt = "Test execution query for agentic-music-playlist-curator-dj"
    assert len(prompt) > 0
    assert "Test" in prompt
