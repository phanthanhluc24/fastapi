from fastapi import Request, status  
from fastapi.responses import JSONResponse  
from jose import JWTError, jwt  
from starlette.middleware.base import BaseHTTPMiddleware  
  
from utils.auth import SECRET_KEY, ALGORITHM, requires_auth, PUBLIC_PATHS  
from repositories.user_repository import UserRepository  
from db.session import SessionLocal  
  
class JWTAuthMiddleware(BaseHTTPMiddleware):  
    async def dispatch(self, request: Request, call_next):  
        # Kiểm tra xem path có cần xác thực không  
        if not requires_auth(request):  
            return await call_next(request)  
  
        # Kiểm tra token  
        auth_header = request.headers.get("Authorization")  
        if not auth_header or not auth_header.startswith("Bearer "):  
            return JSONResponse(  
                status_code=status.HTTP_401_UNAUTHORIZED,  
                content={  
                    "success": False,  
                    "data": None,  
                    "error": {"code": "UNAUTHORIZED", "message": "Not authenticated"}  
                },  
                headers={"WWW-Authenticate": "Bearer"},  
            )  
  
        token = auth_header.replace("Bearer ", "")  
        try:  
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  
            email = payload.get("sub")  
            if email is None:  
                raise JWTError  
                  
            # Kiểm tra user có tồn tại không  
            db = SessionLocal()  
            try:  
                user_repo = UserRepository(db)  
                user = user_repo.get_by_email(email)  
                if user is None:  
                    raise JWTError  
                # Lưu thông tin user vào request state để sử dụng sau này  
                request.state.user = user  
            finally:  
                db.close()  
                  
        except JWTError:  
            return JSONResponse(  
                status_code=status.HTTP_401_UNAUTHORIZED,  
                content={  
                    "success": False,  
                    "data": None,  
                    "error": {"code": "INVALID_TOKEN", "message": "Could not validate credentials"}  
                },  
                headers={"WWW-Authenticate": "Bearer"},  
            )  
  
        # Nếu token hợp lệ, tiếp tục xử lý request  
        return await call_next(request)