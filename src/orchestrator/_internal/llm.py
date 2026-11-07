import asyncio

async def fake_llm(text: str, model: str) -> list[str]:
    await asyncio.sleep(0.1)  # stands in for a real LLM call
    return [f"[{model}] Suggestion for: {text}"]
