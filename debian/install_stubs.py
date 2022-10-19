from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "stub-uploader"))


import os
import re
import shlex
import shutil
import subprocess
import toml
from scripts.build_wheel import main as build_wheel
from scripts.metadata import determine_version


debian = Path(".") / "debian"
install_root = debian / "python3-typeshed"

def run(cmd):
    print(shlex.join(cmd))
    subprocess.check_call(cmd)


provides = []
for stub in sys.argv[1:]:
    metadata = toml.load(f"stubs/{stub}/METADATA.toml")
    version = metadata["version"]
    build_dir = f"debian/build/{stub}"
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    distdir = Path(build_wheel(".", stub, version, build_dir))
    for wheel in distdir.glob("*.whl"):
        cmd = [
            sys.executable,
            "-mpip",
            "install",
            "--system",
            "--no-deps",
            f"--target={install_root}/usr/lib/python3/dist-packages",
            str(wheel),
        ]
        run(cmd)
    virtual_package = "python3-types-" + re.sub(r'[^a-z0-9=]', '-', stub.lower())
    provides.append(f"{virtual_package} (= {version})")

(debian / "python3-typeshed.substvars").write_text(
    "typeshed:Provides=" + ", ".join(provides) + "\n"
)
