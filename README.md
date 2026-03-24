# Open WebUI 项目

> [!note]
> 该项目需要您持有兼容 OpenAI API 返回格式的云端大模型 API 地址和 API Key，或本地运行 Ollama 模型服务。
> 
> 推荐使用智谱平台，该平台提供的部分模型为免费模型：
> - 智谱国内版：https://bigmodel.cn/
> - 智谱国际版：https://z.ai/subscribe

> [!warning]
> 由于 Open WebUI 尚未进入稳定版，当前页内容可能随时发生变更，请严格依据 [Open WebUI 文档](https://docs.openwebui.com/)来使用和进行相关操作。

## 第一次使用？

`uv` 是 Open WebUI 推荐的 Python 包管理器。请先参考 `uv` 官网安装 `uv` Python 包管理器：https://docs.astral.sh/uv/getting-started/installation/

然后，转到该项目，在根目录启动终端并运行以下命令以安装项目依赖：

```bash
uv sync
```

## 启动项目

根据 Open WebUI 文档，请确保 Python 版本为 Python 3.11。过高或过低的 Python 版本可能存在问题。

请先将 `example.env` 文件改名为 `.env` 文件，然后运行以下命令以 `example.env` 环境变量启动项目：

```bash
uv run --env-file .env open-webui serve
```

或：

```bash
uv run main.py
```

首次启动时，Open WebUI 会连接 Hugging Face 下载必要的模型，`example.env` 配置了 Hugging Face 中国大陆镜像加速地址（<https://hf-mirror.com>）。

完成启动后，访问 http://localhost:8080 即可查看该项目。您需要配置外部大模型地址及 API Key，或 Ollama 本地模型 Local Host 服务。

## 参考

- `uv` 文档：https://docs.astral.sh/uv/
- Open WebUI 文档：https://docs.openwebui.com/
