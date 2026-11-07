from importlib.metadata import version
from .contracts import Settings, Suggestion, SuggestionContext, SuggestionPayload
from ._internal.llm import fake_llm

async def build_suggestions(ctx: SuggestionContext, settings: Settings | None = None) -> SuggestionPayload:
    settings = settings or Settings()
    titles = await fake_llm(ctx.text, settings.model)
    return SuggestionPayload(
        record_id=ctx.record_id,
        suggestions=[Suggestion(title=t, score=1.0) for t in titles],
        orchestrator_version=version("orchestrator"),
    )
