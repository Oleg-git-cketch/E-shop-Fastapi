from fastapi import APIRouter


support_router = APIRouter(prefix='/support', tags=["Тех. Поддержка"])

@support_router.get("/bot_link")
async def get_bot_link():
    bot_url = "https://t.me/PySiteSupportBot"
    return {"message": f"Вы можете связаться с нашим ботом по следующей ссылке: {bot_url}"}