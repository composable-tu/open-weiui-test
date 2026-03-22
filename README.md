# Open WebUI 项目

## 第一次使用？

`uv` 是 Open WebUI 推荐的 Python 包管理器。请先参考 `uv` 官网安装 `uv` Python 包管理器：https://docs.astral.sh/uv/getting-started/installation/

然后，转到该项目，在根目录启动终端并运行以下命令以安装项目依赖：

```bash
uv sync
```

## 启动项目

根据 Open WebUI 文档，请确保 Python 版本为 Python 3.11。过高或过低的 Python 版本可能存在问题。

运行以下命令以 `example.env` 环境变量启动项目：

```bash
uv run --env-file example.env open-webui serve
```

首次启动时，Open WebUI 会连接 Hugging Face 下载必要的模型，`example.env` 配置了 Hugging Face 中国大陆镜像加速地址（<https://hf-mirror.com>）。

完成启动后，访问 http://localhost:8080 即可查看该项目。您可能需要配置外部大模型地址及 API Key，或 Ollama 本地模型 Local Host 服务。

## 参考

- `uv` 文档：https://docs.astral.sh/uv/
- Open WebUI 文档：https://docs.openwebui.com/
