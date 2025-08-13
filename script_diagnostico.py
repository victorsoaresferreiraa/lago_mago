import os
import subprocess
import shutil

def check_java_version():
    try:
        output = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT)
        output = output.decode()
        print("✅ Java encontrado:")
        print(output.splitlines()[0])
        if "version \"11" in output:
            print("✔️ Java 11 está ativo.")
        else:
            print("⚠️ Java ativo não é a versão 11. Verifique o JAVA_HOME.")
    except FileNotFoundError:
        print("❌ Java não encontrado. Instale o Java 11 e configure o JAVA_HOME.")

def check_hadoop_home():
    hadoop_home = os.environ.get("HADOOP_HOME")
    if hadoop_home:
        print(f"✅ HADOOP_HOME está definido: {hadoop_home}")
        winutils_path = os.path.join(hadoop_home, "bin", "winutils.exe")
        if os.path.isfile(winutils_path):
            print("✔️ winutils.exe encontrado.")
        else:
            print("❌ winutils.exe não encontrado em HADOOP_HOME/bin.")
    else:
        print("❌ HADOOP_HOME não está definido.")

def check_path_for_winutils():
    found = shutil.which("winutils.exe")
    if found:
        print(f"✅ winutils.exe está no PATH: {found}")
    else:
        print("❌ winutils.exe não está no PATH.")

print("🔍 Verificando ambiente PySpark no Windows...\n")
check_java_version()
print()
check_hadoop_home()
print()
check_path_for_winutils()