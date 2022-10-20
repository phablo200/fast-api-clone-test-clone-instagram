hash:
	openssl rand -hex 32
server:
	uvicorn main:app --reload
