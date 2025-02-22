from config import load_config
from models.user import User
from utils.di import get_user_repository
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


config = load_config()
user_repo = get_user_repository(config.get("data_source"))

class UserAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/users":
            users = user_repo.get_all_users()
            self._set_headers()
            self.wfile.write(json.dumps(users).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "404"}).encode())

    def do_POST(self):
        if self.path == "/users":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                if not data.get("first_name") or not data.get("last_name") or not data.get("email"):
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "Missing or invalid data"}).encode())
                    return
                user = User(
                    first_name=data.get("first_name"),
                    last_name=data.get("last_name"),
                    email=data.get("email")
                )
                created_user = user_repo.create_user(user)
                self._set_headers(201)
                self.wfile.write(json.dumps(created_user).encode())
            except Exception as e:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid data format or internal server problem"}).encode())

def run(server_class=HTTPServer, handler_class=UserAPIHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server works at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
