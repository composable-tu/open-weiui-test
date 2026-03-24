import subprocess
import sys
from pathlib import Path


def main():
    # 获取脚本所在目录
    script_dir = Path(__file__).parent.resolve()

    # Tika JAR 文件路径
    tika_jar = script_dir / "tika-server-standard-3.3.0.jar"

    # 检查 JAR 文件是否存在
    if not tika_jar.exists():
        print(f"Error: Tika JAR file not found: {tika_jar}")
        sys.exit(1)

    # 构建命令
    cmd = ["java", "-jar", str(tika_jar), "--host", "0.0.0.0", "--port", "9998"]

    print(f"Starting Apache Tika server on 0.0.0.0:9998...")
    print(f"Using JAR: {tika_jar}")

    try:
        # 启动 Tika 服务器
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Tika server: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nShutting down Tika server...")
        sys.exit(0)


if __name__ == "__main__":
    main()
