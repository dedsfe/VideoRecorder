
Flask + OpenCV Video Recorder

Um projeto simples que integra Flask e OpenCV para:
- Fazer streaming ao vivo da câmera via MJPEG.
- Controlar início e fim da gravação com rotas HTTP (`/start` e `/stop`).
- Salvar os vídeos gravados no servidor (pasta `clips/`).

## 🚀 Tecnologias
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)

## 📂 Estrutura do Projeto
```

/app.py                # Backend Flask
/templates/view\.html   # Interface HTML simples
/static/main.js        # Scripts do frontend
/clips/                # Onde os vídeos são salvos (não versionado)
requirements.txt       # Dependências

````

## 🔧 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/video-recorder-flask.git
   cd video-recorder-flask
````

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o servidor:

   ```bash
   python app.py
   ```

5. Acesse em [http://localhost:8000](http://localhost:8000).

## ▶️ Como usar

* `/` → Interface com preview do vídeo.
* `/video` → Streaming MJPEG.
* `POST /start` → Inicia gravação e cria arquivo em `clips/`.
* `POST /stop` → Para gravação, fecha o arquivo e retorna metadados (`path`, `duration_sec`, `size_bytes`).

Exemplo com `curl`:

```bash
curl -X POST http://localhost:8000/start
sleep 10
curl -X POST http://localhost:8000/stop
```

O vídeo gravado ficará disponível em `clips/`.

## 📌 Limitações atuais

* Só funciona com a câmera local (não em cloud direto).
* Sem autenticação (qualquer um pode chamar as rotas).
* Apenas uma gravação por vez.

## 📅 Roadmap

* [ ] Rota `/status` (mostrar se está gravando, tempo e fps).
* [ ] Rota `/last` (download do último clipe).
* [ ] Interface com botão de **Start/Stop** e indicador de REC.
* [ ] Upload dos clipes para AWS S3.
* [ ] Suporte a streams RTSP em vez da câmera local.


