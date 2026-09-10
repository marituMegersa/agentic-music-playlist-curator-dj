from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.music_playlist_curator_dj.models import AgenticMusicPlaylistCuratorDjSession, AgenticMusicPlaylistCuratorDjItem
from app.domain.music_playlist_curator_dj.schemas import AgenticMusicPlaylistCuratorDjSessionCreate, AgenticMusicPlaylistCuratorDjItemCreate

class AgenticMusicPlaylistCuratorDjService:
    @staticmethod
    def create_session(db: Session, data: AgenticMusicPlaylistCuratorDjSessionCreate) -> AgenticMusicPlaylistCuratorDjSession:
        db_obj = AgenticMusicPlaylistCuratorDjSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticMusicPlaylistCuratorDjSession:
        return db.query(AgenticMusicPlaylistCuratorDjSession).filter(AgenticMusicPlaylistCuratorDjSession.id == session_id).first()
