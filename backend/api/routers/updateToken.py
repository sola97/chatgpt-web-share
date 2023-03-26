
from fastapi import APIRouter
from pydantic import BaseModel
import api.globals as g
router = APIRouter()

class TokenUpdateRequest(BaseModel):
    puid: str
    accessToken: str

@router.post('/updateToken', response_model=dict)
async def update_token(request: TokenUpdateRequest):
    puid = request.puid
    access_token = request.accessToken
    g.config.set('reverse_proxy_puid', puid)
    g.config.set('chatgpt_access_token', access_token)
    g.config.save(g.config_file)
    return {"message": "Configuration updated successfully."}
