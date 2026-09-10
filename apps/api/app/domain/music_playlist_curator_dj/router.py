from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.music_playlist_curator_dj.schemas import AgenticMusicPlaylistCuratorDjSessionCreate, AgenticMusicPlaylistCuratorDjSessionResponse
from app.domain.music_playlist_curator_dj.service import AgenticMusicPlaylistCuratorDjService

router = APIRouter(prefix="/api/v1/music_playlist_curator_dj", tags=["Agentic Music Playlist Curator Dj Domain"])

@router.post("/sessions", response_model=AgenticMusicPlaylistCuratorDjSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticMusicPlaylistCuratorDjSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Music Playlist Curator Dj.
    """
    return AgenticMusicPlaylistCuratorDjService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticMusicPlaylistCuratorDjSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticMusicPlaylistCuratorDjService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
