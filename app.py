from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🎓 CertiSign Academic</h1>
    <p>Sistem Sertifikat Digital Mahasiswa</p>
    """

if __name__ == '__main__':
    app.run()
