import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def main():
    # 获取项目根目录
    project_root = Path(__file__).parent

    # 设置日志文件路径
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = project_root / f"open-webui_{timestamp}.log"

    print(f"Starting Open WebUI server...")
    print(f"Log file: {log_file}")

    # 构建命令
    cmd = ["uv", "run", "--env-file", ".env", "open-webui", "serve"]

    try:
        # 打开日志文件
        with open(log_file, "w", encoding="utf-8") as f:
            # 执行命令
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=project_root,
                                       env={**os.environ, **read_env_file(project_root / ".env")})

            print(f"Server started with PID: {process.pid}")
            print("Logs are being saved to:", log_file)
            print("\nPress Ctrl+C to stop the server")
            print("-" * 50)

            # 实时读取输出并同时写入控制台和文件
            if process.stdout:
                for line in process.stdout:
                    # 解码字节为字符串
                    text_line = line.decode("utf-8", errors="replace")

                    # 写入文件
                    f.write(text_line)
                    f.flush()

                    # 输出到控制台（去掉末尾换行符避免重复）
                    print(text_line, end="")

            process.wait()

    except KeyboardInterrupt:
        print("\nShutting down server...")
        if 'process' in locals():
            process.terminate()
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)


def read_env_file(env_path):
    """读取.env 文件并返回环境变量的字典"""
    env_vars = {}
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "=" in line:
                        key, value = line.split("=", 1)
                        # 移除引号
                        value = value.strip("'\"")
                        env_vars[key.strip()] = value
    return env_vars


if __name__ == "__main__":
    main()
